# -*- coding: utf-8 -*-
"""
@author: Leo
Date:  2019/3/2
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os
import  numpy
import cv2
import matplotlib.pyplot as plt
import PIL.Image

class MainRun():
    _dir = os.path.dirname(os.path.dirname(os.getcwd()))
    _imgSrc = os.path.join(_dir, u"ShareMedia/Images/cat1.jpg")
    _imgDst = os.path.join(_dir,u"ShareMedia/Images/cat1_diff.jpg")

    @classmethod
    def runDemo(cls):
        print("hello world")

    @classmethod
    def showMatrix(cls):
        print numpy.zeros((4,4),dtype=numpy.int)
        print numpy.ones((3,3),dtype=numpy.float)
        print numpy.arange(1,10,1).reshape((3,3))
        print numpy.linspace(10,20,10)
        numpy.ones((3,3)) - numpy.zeros((3,3))


    @classmethod
    def showImgDiff(cls):
        lSrc = cv2.imread(cls._imgSrc)
        lDst = cv2.imread(cls._imgDst)
        lSrcB, lSrcG,lSrcR = cv2.split(lSrc)
        lDstB, lDstG,lDstR = cv2.split(lDst)
        lSrc = cv2.cvtColor(lSrc,cv2.COLOR_BGR2GRAY)
        lDst = cv2.cvtColor(lDst,cv2.COLOR_BGR2GRAY)



        lDiff = numpy.array(lDstB,dtype=numpy.int64)  - numpy.array(lSrcB,dtype=numpy.int64)
        lSortDiff = numpy.clip(lDiff,0,255)
        # lSortDiff = numpy.array(lSortDiff,dtype=numpy.uint8)
        # lSortDiff = numpy.clip(lSortDiff,0,255)
        # lGray = cv2.cvtColor(lSortDiff,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('diff',lGray)
        # cv2.imshow("src",lSrc)
        # cv2.imshow("dst",lDst)
        # cv2.imshow('rgbdiff',lSortDiff)
        # cv2.waitKey(0)
        plt.subplot(221),plt.imshow(lSrcB,cmap ='gray')
        plt.subplot(222),plt.imshow(lDstB,cmap ='gray')
        plt.subplot(223),plt.imshow(lDiff,cmap ='gray')
        plt.subplot(224),plt.imshow(lSortDiff,cmap ='gray')
        plt.show()

    @classmethod
    def showImgDiffByCv2(cls):
        lSrc = cv2.imread(cls._imgSrc)
        lDst = cv2.imread(cls._imgDst)

        lSortDiff = cv2.absdiff(lSrc,lDst)
        # lGray = cv2.cvtColor(lSortDiff, cv2.COLOR_BGR2GRAY)
        cv2.imshow('diff', lSortDiff)
        # cv2.imshow('rgbdiff', lDst)
        cv2.waitKey(0)

    @classmethod
    def showImgDiffPil(cls):

        lSrc = PIL.Image.open(cls._imgSrc)
        lDst = PIL.Image.open(cls._imgDst)
        # lSrc = cv2.cvtColor(lSrc, cv2.COLOR_BGR2GRAY)
        # lDst = cv2.cvtColor(lDst, cv2.COLOR_BGR2GRAY)
        # lShape = lSrc.shape
        # lDiff = lDst - lSrc
        lDiff = numpy.array(lDst, dtype=numpy.float64) - numpy.array(lSrc, dtype=numpy.float64)
        lSortDiff = numpy.clip(lDiff, 0, 255)
        # lGray = cv2.cvtColor(lSortDiff,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('diff',lGray)
        # cv2.imshow("src",lSrc)
        # cv2.imshow("dst",lDst)
        # cv2.imshow('rgbdiff',lSortDiff)
        # cv2.waitKey(0)
        plt.subplot(221), plt.imshow(lSrc)
        plt.subplot(222), plt.imshow(lDst)
        plt.subplot(223), plt.imshow(lDiff)
        plt.subplot(224), plt.imshow(lSortDiff)
        plt.show()





if __name__ == '__main__':
    MainRun.runDemo()
    # MainRun.showMatrix()
    MainRun.showImgDiff()
    # MainRun.showImgDiffByCv2()
    # MainRun.showImgDiffPil()