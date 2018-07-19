# -*- coding: utf-8 -*-

import sys, os, time

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

def showHistByOrigin(tImage):

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


def showHist(tImage):
    if os.path.exists(tImage) is False:
        print(u"%s not found" % tImage)
        return
    lImge = cv2.imread(tImage)
    lImge = cv2.cvtColor(lImge,cv2.COLOR_RGB2GRAY)
    # if __debug__:
    #     cv2.imshow("display",lImge)
    img = np.array(lImge)
    plt.figure('cat')
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, density=1, facecolor='green', alpha=0.75)
    plt.show()



class MainRun():
    @staticmethod
    def runShowHist():
        lCurDir = os.getcwd()
        lTarDir = os.path.dirname(os.path.dirname(lCurDir))
        lFile = os.path.join(lTarDir,u"ShareMedia/Images/cat0.jpg")
        showHist(lFile)


if __name__ == "__main__":
    print(os.getcwd())
    MainRun.runShowHist()