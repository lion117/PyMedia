# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging

gLogger = logging.getLogger("pylog")
gLogger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)  #默认是sys.stderr
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('pylog.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

gLogger.addHandler(rf_handler)
gLogger.addHandler(f_handler)

import matplotlib.pyplot as plt
class MainRun():

    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")
    _img1 = os.path.join(_tarDir, u"ShareMedia/Images/cat0.bmp")
    _img2 = os.path.join(_tarDir, u"ShareMedia/Images/cat0_1.bmp")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")

    @classmethod
    def testImageDiff(cls):
        lObjImg1 = cv2.imread(cls._img1)
        lObjImg2 = cv2.imread(cls._img2)
        print(lObjImg1[10,10,0], lObjImg2[10,10,0])
        lObjDiff = lObjImg1 - lObjImg2

        plt.subplot(1,3,1)
        plt.imshow(lObjImg1[:,:,::-1])
        plt.subplot(1,3,2)
        plt.imshow(lObjImg2[:,:,::-1])
        plt.subplot(1,3,3)
        plt.imshow(lObjDiff[:,:,::-1])
        plt.show()



if __name__ == "__main__":
    MainRun.runTest()
    MainRun.testImageDiff()