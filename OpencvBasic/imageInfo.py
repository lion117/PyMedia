# -*- coding: utf-8 -*-

import sys, os, time

import cv2

class MainRun():
    lImgDir = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/Images")
    _img = os.path.join(lImgDir, u"dog0.jpg")


    @classmethod
    def testImgStatue(cls):
        lImg = cv2.imread(cls._img)
        print(lImg.dtype)
        print(lImg.item(100,100,0))
        print(lImg.shape)
        print(lImg.size)

    @classmethod
    def testImgPointOption(cls):
        lImg = cv2.imread(cls._img)
        cv2.imshow("origin", lImg)
        print("origin: %d"%lImg.item(100,100,0))
        lImg.itemset((100,100,0),255)
        print("dest: %d"%lImg.item(100,100,0))
        # for i in range(100,150):
        #     lImg.itemset((100,i,0),255)
        #
        # cv2.imshow("modify", lImg)
        #
        #
        #
        # cv2.waitKey(0)
        # cv2.release()
        # cv2.destroyAllWindows()

    @classmethod
    def testRoiOption(cls):
        lImg = cv2.imread(cls._img)
        lEye =lImg[10:30,10:30]
        lImg[40:40,50:50]=lEye

        cv2.imshow("rio", lEye)
        cv2.waitKey(0)
        cv2.release()
        cv2.destroyAllWindows()

    @classmethod
    def testSplit(cls):
        lImg = cv2.imread(cls._img)
        lr = lImg[:,:,0]
        # lg= lImg[:,:,1]
        # lb= lImg[:,:,2]
        lImg[:,:,0] = 0
        lImg[:,:,1] = 0
        # lImg[:,:,2] = 0
        cv2.imshow('r', lImg)
        # cv2.imshow('g',lg)
        # cv2.imshow('b',lb)
        cv2.waitKey(0)
        cv2.release()
        cv2.destroyAllWindows()








if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.testOpenCamera()
    # MainRun.testOpenVideo()
    MainRun.testImgStatue()
    # MainRun.testImgPointOption()
    # MainRun.testRoiOption()
    # MainRun.testSplit()
