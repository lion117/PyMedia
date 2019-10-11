# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
import matplotlib.pyplot as plt

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


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")


    @classmethod
    def testNumpyMath(cls):
        lx = numpy.linspace(0.000001,100,num= 1000)
        ly = numpy.log10(lx)
        plt.plot(lx,ly)
        plt.show()



if __name__ == "__main__":
    MainRun.runTest()
    MainRun.testNumpyMath()