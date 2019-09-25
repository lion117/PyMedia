# -*- coding: utf-8 -*-

import sys, os, time
import cv2

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0.jpg")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def learnYuvMat(cls):
        imgMat = cv2.imread(cls._img)
        yuvMat = cv2.cvtColor(imgMat, cv2.COLOR_BGR2YUV_I420)
        cv2.imshow("bgr", imgMat)
        cv2.imshow("yuv", yuvMat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()





if __name__ == "__main__":
    MainRun.runTest()
    MainRun.learnYuvMat()