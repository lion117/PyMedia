# -*- coding: utf-8 -*-

import sys, os, time


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

def ConvertHist(tImage):

    if os.path.exists(tImage) is False:
        print(u"%s not found"%tImage)
        return
    lImge = Image.open(tImage).convert('L')
    if __debug__:
        lImge.show()
    img = np.array(lImge)
    plt.figure('cat')
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, density=1, facecolor='green', alpha=0.75)
    plt.show()


def convertGrayByCv(tImage):
    if os.path.exists(tImage) is False:
        print(u"%s not found" % tImage)
        return

def cvRGBTest():
    lParentDir = os.path.dirname(os.path.dirname(os.getcwd()))
    lImageDir = os.path.join(lParentDir,u"ShareMedia/Images")
    lFile = os.path.join(lImageDir,u"dog1.jpg")
    lImage1 = Image.open(lFile)
    lImage2 = cv2.imread(lFile)
    lImage3 = Image.fromarray(cv2.cvtColor(lImage2, cv2.COLOR_BGR2RGB))
    lImage4 =Image.fromarray(lImage2)

    plt.subplot(221),plt.imshow(lImage3)
    plt.subplot(222),plt.imshow(lImage4)
    plt.subplot(223),plt.imshow(lImage1)
    plt.subplot(224),plt.imshow(lImage2)
    plt.show()




class MainTest():
    @staticmethod
    def runConvertHist():
        lImage = u"hongkong.jpg"
        ConvertHist(lImage)

if __name__ == "__main__":
    print os.getcwd()
    MainTest.runConvertHist()
    # cvRGBTest()