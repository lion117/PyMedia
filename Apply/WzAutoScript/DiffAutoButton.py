# -*- coding: utf-8 -*-
import cv2
import sys, os, time
import  matplotlib.pyplot as plt

class MainRun():
    _tarDir = os.path.dirname(os.path.dirname(os.getcwd()))
    _cut0Img = os.path.join(_tarDir, u"ShareMedia/Images/auto0.png")
    _cut1Img = os.path.join(_tarDir, u"ShareMedia/Images/auto1.png")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def cutImgFromBk(cls,tSrc):
        pass

    @classmethod
    def calImgThreadhold(cls):
        lImgcut0 = cv2.imread(cls._cut0Img)
        (lcut0B,lcut0R,lcut0G) = cv2.split(lImgcut0)
        lImgcut1 = cv2.imread(cls._cut1Img)
        (lcut1B,lcut1R,lcut1G) = cv2.split(lImgcut0)
        plt.figure()
        plt.subplot(1,2,1)
        plt.imshow(lcut1R)
        plt.subplot(1,2,2)
        plt.imshow(lcut1B)
        plt.show()

    @classmethod
    def calMean(cls, tImgObj):
        lMean = cv2.mean(cv2.split(tImgObj)[0])[0]
        # lImg0 = cv2.imread(cls._cut0Img)
        # lImg1 = cv2.imread(cls._cut1Img)
        # lMean0 = cv2.mean(cv2.split(lImg0)[0])[0]
        # lMean1 = cv2.mean(cv2.split(lImg1)[0])[0]
        # print(lMean0,lMean1)
        return lMean







if __name__ == "__main__":
    # MainRun.runTest()
    # MainRun.calImgThreadhold()
    MainRun.calMean(None)
