# -*- coding: utf-8 -*-

import sys, os, time
import  cv2
import numpy as np


def linerGrayApi(tImage):
    lImg = cv2.imread(tImage)
    larrImg = np.array(lImg)
    cv2.imshow('display',larrImg)
    cv2.waitKey(0)

class MainRun():
    lCurDir = os.getcwd()
    lTarDir = os.path.dirname(os.path.dirname(lCurDir))
    @classmethod
    def runLinerGray(cls):
        lFile = os.path.join(cls.lTarDir,u"ShareMedia/Images/cat0_gray.jpg")
        linerGrayApi(lFile)



if __name__ == "__main__":
    print(os.getcwd())
    MainRun.runLinerGray()