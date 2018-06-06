# -*- coding: utf-8 -*-

import os

import cv2
import imutils
import numpy
from PIL import  Image

def locateImage(tSrouce, tTarget):
    imgSrc = cv2.imread(tSrouce, 0)
    imgTarget = cv2.imread(tTarget, 0)


    # w, h = imgTarget.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    method = eval(methods[0])
    # Apply imgTarget Matching
    res = cv2.matchTemplate(imgSrc, imgTarget, method)


    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val < 0.95:
        print (u"failed to find the image ")
        return (False,0,0)

    data =res.any()
    lTemp  = Image.open(tTarget)
    width , height = lTemp.size
    lx = max_loc[0] + width/2
    ly = max_loc[1] + height/2
    return (True , lx, ly)


def isImageDiffMuch(tImgFirst, tImgSecond):
    if os.path.exists(tImgFirst) is False or os.path.exists(tImgSecond) is False:
        print (u"image is not exist")
        return  (False , -1)

    lMiniArea = 150
    lGrabValue = 80
    lFirst = cv2.imread(tImgFirst, cv2.IMREAD_GRAYSCALE  )
    lSecond = cv2.imread(tImgSecond, cv2.IMREAD_GRAYSCALE )
    lHeight = lFirst.shape[0]
    lWidth = lFirst.shape[1]
    # showImg(lFirst)
    # showImg(lSecond)

    lSecond = adjustImg(lFirst, lSecond)
    # showImg(lFirst)
    # showImg(lSecond)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lFirst = cv2.GaussianBlur(lFirst, (21, 21), 0)
    lSecond = cv2.GaussianBlur(lSecond, (21, 21), 0)

    # showImg(lFirst)
    # showImg(lSecond)

    frameDelta = cv2.absdiff(lFirst, lSecond)
    thresh = cv2.threshold(frameDelta, lGrabValue, 255, cv2.THRESH_BINARY)[1]
    # 扩展阀值图像填充孔洞，然后找到阀值图像上的轮廓
    thresh = cv2.dilate(thresh, None, iterations=2)
    (image, contours, hierarchy) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # showImg(image)

    lFindDiff =False
    lDiffValue = 0
    for c in contours:
        # if the contour is too small, ignore it
        area = cv2.contourArea(c)
        if area >= lDiffValue:
            lDiffValue = area

        if area < lMiniArea:
            continue
        else:
            lFindDiff = True
    return (lFindDiff , lDiffValue)




def showImg(tImg):
    cv2.imshow("Image",tImg)
    cv2.waitKey(0)


def adjustImg(lFirst, lSecond):

    lHeight = lFirst.shape[0]
    lWidth = lFirst.shape[1]

    lHeight1 = lSecond.shape[0]
    lWidth1 = lSecond.shape[1]

    if lHeight  <=  lWidth and lHeight1 <=  lWidth1 :
        lSecond = imutils.resize(lSecond, width=lWidth, height=lHeight)

    elif lHeight  >=  lWidth and lHeight1 >=  lWidth1 :
        lSecond = imutils.resize(lSecond, width=lWidth, height=lHeight)

    else:
        # lSecond = imutils.rotate(lSecond, angle= -90)
        lSecond= numpy.rot90(lSecond)
        lSecond = imutils.resize(lSecond, width=lWidth, height=lHeight)

    return  lSecond



class MainTest():
    @staticmethod
    def testLocateImage():
        lSrc = u"game.png"
        lTarget  = u"test/continue.png"
        print locateImage(lSrc, lTarget)

    @staticmethod
    def testFindImgfromImg():
        from image import imagecompare
        lSrc = u"game2.png"
        lTarget  = u"test/icon.png"
        print imagecompare.FindImgFromImg(lSrc, lTarget)

    @staticmethod
    def testFindDiff():
        lFirst = u"template.png"
        lSecond = u"game2.png"
        print isImageDiffMuch(lFirst, lSecond)

if __name__ == "__main__":
    print os.getcwd()
    # MainTest.testLocateImage()
    # MainTest.testFindImgfromImg()
    MainTest.testFindDiff()