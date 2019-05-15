# -*- coding: utf-8 -*-

import sys, os, time
import cv2
import numpy as np

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _imggirl720p = os.path.join(_tarDir, u"ShareMedia/Images/girl720p.png")
    _imggirl1080p = os.path.join(_tarDir, u"ShareMedia/Images/girl1080p.png")
    _imgboy720p = os.path.join(_tarDir, u"ShareMedia/Images/boy720p.png")
    _imgboy1080p = os.path.join(_tarDir, u"ShareMedia/Images/boy1080p.png")
    _imgmomo = os.path.join(_tarDir, u"ShareMedia/Images/momo.jpg")
    _imgmomo101 = os.path.join(_tarDir, u"ShareMedia/Images/momo_101.jpg")
    _imgmomo010 = os.path.join(_tarDir, u"ShareMedia/Images/momo_010.jpg")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def computeCanny(cls):
        imgboy720p = cv2.imread(cls._imgboy720p)
        imgboy1080p = cv2.imread(cls._imgboy1080p)
        v720p,cboy720 = MainRun.GetCannyMax(imgboy720p)
        v1080p,cboy1080 = MainRun.GetCannyMax(imgboy1080p)
        print("boys: 720:%f, 1080p:%f"%(v720p, v1080p))

        imggirl720p = cv2.imread(cls._imggirl720p)
        imggirl1080p = cv2.imread(cls._imggirl1080p)
        v720p1,vgirl720 = MainRun.GetCannyMax(imggirl720p)
        v1080p1,vgirl1080 = MainRun.GetCannyMax(imggirl1080p)
        print("girl 720:%f, 1080p:%f"%(v720p1, v1080p1))

        imgmomo = cv2.imread(cls._imgmomo)
        imgmomo101 = cv2.imread(cls._imgmomo101)
        imgmomo010 = cv2.imread(cls._imgmomo010)
        vmomo, vCannymomo = MainRun.GetCannyMax(imgmomo)
        vmomo101, vCannymomo101 = MainRun.GetCannyMax(imgmomo101)
        vmomo010, vCannymomo010 = MainRun.GetCannyMax(imgmomo010)
        print("momo  0:%f, 101:%f, 010:%f"%(vmomo, vmomo101, vmomo010))


        cv2.imwrite("canny_cboy720.png",cboy720)
        cv2.imwrite("canny_cboy1080.png",cboy1080)
        cv2.imwrite("canny_vgirl720.png",vgirl720)
        cv2.imwrite("canny_vgirl1080.png",vgirl1080)
        cv2.imwrite("canny_vmomo.png",vCannymomo)
        cv2.imwrite("canny_vmomo101.png",vCannymomo101)
        cv2.imwrite("canny_vmomo010.png",vCannymomo010)



    @classmethod
    def GetCannyMax(cls, tImg):
        img = cv2.GaussianBlur(tImg, (3, 3), 0)
        # img = np.array(img,dtype=np.int8)
        yuv420= cv2.cvtColor(tImg, cv2.COLOR_BGR2YUV)
        yMat,uMat,vMat = cv2.split(yuv420)
        canny = cv2.Canny(yMat, 50, 150)
        # cv2.imshow("test", canny)
        # cv2.waitKey(2000)
        return (np.mean(canny), canny)







if __name__ == "__main__":
    MainRun.runTest()
    MainRun.computeCanny()