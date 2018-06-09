# -*- coding: utf-8 -*-

import sys, os, time

import cv2
from PIL import  Image

def imageRotate(tImage):
    if os.path.exists(tImage) is False:
        print (u"image not exist")
        return

    lImg = Image.open(tImage)
    width, height = lImg.size


def imageRotateByCv(tImage):
    if os.path.exists(tImage) is False:
        print (u"image not exist")
        return
    lImg = cv2.imread(tImage)
    lHeight = lImg.shape[0]
    lWidth = lImg.shape[1]



class MainTest():
    @staticmethod
    def testImageRotate():
        lImge = u"screenshot.png"



if __name__ == "__main__":
    print os.getcwd()