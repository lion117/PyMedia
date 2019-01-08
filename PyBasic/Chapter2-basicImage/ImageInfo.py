# -*- coding: utf-8 -*-

import sys, os, time
from  PIL import  Image
import  cv2
import numpy as np


def getImageSize(tFile):
    if False:
        lImg =  Image.open(tFile)
        (lWidth, lHeight) = lImg.size
        lFormat = lImg.format
    else:
        lImg = cv2.imread(tFile,0)
        lHeight , lWidth  = lImg.shape[:2]
    return  (lWidth , lHeight)


def showImage(tFile):
    lImg =  cv2.imread(tFile)
    cv2.imshow('show', lImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showImageObj(tCVObj):
    cv2.imshow('show', tCVObj)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convertGray(tFile):
    lImage = cv2.imread(tFile)
    lGray = cv2.cvtColor(lImage,cv2.COLOR_RGB2GRAY)
    showImageObj(lGray)
    return  lGray


def convertGrayToRGB(tFile):
    lImage = cv2.imread(tFile)
    lRGB = cv2.cvtColor(lImage,cv2.COLOR_GRAY2RGB)
    showImageObj(lRGB)
    return  lRGB


class MainRun():
    @staticmethod
    def runGetImageSize():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir,u"ShareMedia/Images/cat0.jpg")
        print getImageSize(lFile)

    @staticmethod
    def runShowImage():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir, u"ShareMedia/Images/cat0_gray.jpg")
        showImage(lFile)


    @staticmethod
    def runConvertGray():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir, u"ShareMedia/Images/cat0.jpg")
        convertGray(lFile)

    @staticmethod
    def runConvertGrayImage():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir, u"ShareMedia/Images/cat0.jpg")
        lDstFile = os.path.join(lTarDir, u"ShareMedia/Images/cat0_gray.jpg")
        lObj = convertGray(lFile)
        cv2.imwrite(lDstFile, lObj)

    @staticmethod
    def runConvertGrayImage():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir, u"ShareMedia/Images/cat0_gray.jpg")
        convertGrayToRGB(lFile)


if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.runGetImageSize()
    # MainRun.runShowImage()
    # MainRun.runConvertGray()
    # MainRun.runConvertGrayImage()
    MainRun.runConvertGrayImage()