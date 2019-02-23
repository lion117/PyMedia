# -*- coding: utf-8 -*-
"""
@author: Leo
Date:  2019/2/23
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os,sys

import cv2

sys.path.insert(0,os.path.dirname(os.path.dirname(os.getcwd())))


from  image.SiftMatch import findMatchImgXY



class MainRun():
    _imgAuto = os.path.join(os.getcwd(),u"feature2.png")
    _imgSrc = os.path.join(os.getcwd() , u"startPic.png")



    @classmethod
    def runDemo(cls):
        print("hello world")


    @classmethod
    def findTarget(cls):
        if os.path.exists(cls._imgAuto) is False or os.path.exists(cls._imgSrc) is False:
            print(u"not find the target images")
            return

        # lSrcImg = cv2.imread(cls._imgAuto)
        # cv2.imshow("src",lSrcImg)
        # cv2.waitKey(1000)


        try:
            (lRet, lx, ly) = findMatchImgXY(cls._imgAuto, cls._imgSrc)
            if lRet is True:
                lSrcObj = cv2.imread(cls._imgSrc)
                lX0 , lY0= lx-25, ly-25
                lX1, lY1 = lx+25,ly+25
                lCutImg = lSrcObj[lY0:lY1, lX0:lX1]


                lDest = cv2.rectangle(lSrcObj, (lx-25,ly-25),(lx+25,ly+25),(0,255,0),2)
                cv2.imshow("find",lCutImg)
                cv2.waitKey(10000)

        except Exception, exInfo:
            print (u"excepiton %s" % (exInfo))

    @classmethod
    def calAverage(cls):
        lImg = cv2.imread(cls._imgAuto)
        mean = cv2.mean(lImg)[0]
        print mean








if __name__ == '__main__':
    MainRun.runDemo()
    MainRun.findTarget()
    # MainRun.calAverage()
