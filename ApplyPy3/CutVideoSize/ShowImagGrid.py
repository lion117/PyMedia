# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
import  matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
gLogger = logging.getLogger(__name__)


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")

    @classmethod
    def testImageGridDemo(cls):
        x = numpy.arange(0,1,0.05)
        y = numpy.power(x, 2)
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(numpy.arange(0,1,0.1))
        ax.set_yticks(numpy.arange(0,1.,0.1))
        plt.scatter(x,y)
        plt.grid()
        plt.show()

    @classmethod
    def testImageGridImage(cls):
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(numpy.arange(0, 1, 0.1))
        ax.set_yticks(numpy.arange(0, 1., 0.1))
        lImgObj = cv2.imread(cls._img)
        plt.imshow(lImgObj)
        plt.grid()
        plt.show()



if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.testImageGridDemo()
    MainRun.testImageGridImage()