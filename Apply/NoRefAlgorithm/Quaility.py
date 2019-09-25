# -*- coding: utf-8 -*-

import sys, os, time
import cv2
import numpy as np

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _imggirl720p = os.path.join(_tarDir, u"ShareMedia/Images/girl720p.png")
    _imggirl1080p = os.path.join(_tarDir, u"ShareMedia/Images/girl1080p.png")
    _imgboy720p = os.path.join(_tarDir, u"ShareMedia/Images/boy720p.png")
    _imgboy1080p = os.path.join(_tarDir, u"ShareMedia/Images/boy1080p.png")
    _imgmomo = os.path.join(_tarDir, u"ShareMedia/Images/momo.jpg")
    _imgmomo101 = os.path.join(_tarDir, u"ShareMedia/Images/momo_101.jpg")
    _imgmomo010 = os.path.join(_tarDir, u"ShareMedia/Images/momo_010.jpg")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def computeCanny(cls):
        imgboy720p = cv2.imread(cls._imgboy720p)
        imgboy1080p = cv2.imread(cls._imgboy1080p)
        v720p,cboy720 = MainRun.GetCannyMax(imgboy720p)
        v1080p,cboy1080 = MainRun.GetCannyMax(imgboy1080p)
        print("boys: 720:%f, 1080p:%f"%(v720p, v1080p))

        imggirl720p = cv2.imread(cls._imggirl720p)
        imggirl1080p = cv2.imread(cls._imggirl1080p)
        v720p1,vgirl720 = MainRun.GetCannyMax(imggirl720p)
        v1080p1,vgirl1080 = MainRun.GetCannyMax(imggirl1080p)
        print("girl 720:%f, 1080p:%f"%(v720p1, v1080p1))

        imgmomo = cv2.imread(cls._imgmomo)
        imgmomo101 = cv2.imread(cls._imgmomo101)
        imgmomo010 = cv2.imread(cls._imgmomo010)
        vmomo, vCannymomo = MainRun.GetCannyMax(imgmomo)
        vmomo101, vCannymomo101 = MainRun.GetCannyMax(imgmomo101)
        vmomo010, vCannymomo010 = MainRun.GetCannyMax(imgmomo010)
        print("momo  0:%f, 101:%f, 010:%f"%(vmomo, vmomo101, vmomo010))


        cv2.imwrite("canny_cboy720.png",cboy720)
        cv2.imwrite("canny_cboy1080.png",cboy1080)
        cv2.imwrite("canny_vgirl720.png",vgirl720)
        cv2.imwrite("canny_vgirl1080.png",vgirl1080)
        cv2.imwrite("canny_vmomo.png",vCannymomo)
        cv2.imwrite("canny_vmomo101.png",vCannymomo101)
        cv2.imwrite("canny_vmomo010.png",vCannymomo010)


    @classmethod
    def calculateSrc(cls):
        lImg1 = os.path.join(os.getcwd(), u"1.png")
        lImg2 = os.path.join(os.getcwd(), u"2.png")

        lImg1Obj = cv2.imread(lImg1)
        lImg2Obj = cv2.imread(lImg2)
        v720p, cobj1 = MainRun.GetCannyMax(lImg1Obj)
        v1080p, cobj2 = MainRun.GetCannyMax(lImg2Obj)
        print("1: 720:%f, 2:%f"%(v720p, v1080p))

        cv2.imwrite("canny_1.png",cobj1)
        cv2.imwrite("canny_2.png",cobj2)

    @classmethod
    def GetCannyMax(cls, tImg):
        img = cv2.GaussianBlur(tImg, (3, 3), 0)
        # img = np.array(img,dtype=np.int8)
        yuv420= cv2.cvtColor(tImg, cv2.COLOR_BGR2YUV)
        yMat,uMat,vMat = cv2.split(yuv420)
        canny = cv2.Canny(yMat, 50, 150)
        # cv2.imshow("test", canny)
        # cv2.waitKey(2000)
        return (np.mean(canny), canny)

    @classmethod
    def computeCannyApi(cls):
        pic1 = os.path.join(os.getcwd(), u"540x960.png")
        pic2 = os.path.join(os.getcwd(), u"720x1280.png")

        imgObj1 = cv2.imread(pic1)
        imgObj2 = cv2.imread(pic2)
        value1, img1 = MainRun.GetCannyMax(imgObj1)
        value2, img2 = MainRun.GetCannyMax(imgObj2)
        print("pic1:%f, pic2:%f" % (value1, value2))
        cv2.imwrite("540x960_out.png", img1)
        cv2.imwrite("720x1280_out.png", img2)






if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.computeCanny()
    # MainRun.calculateSrc()
    MainRun.computeCannyApi()