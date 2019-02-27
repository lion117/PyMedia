# -*- coding: utf-8 -*-

import sys, os, time



class MainRun():
    _tarDir = os.path.dirname(os.path.dirname(os.getcwd()))
    _cut0Img = os.path.join(_tarDir, u"ShareMedia/Images/auto0.png")
    _cut1Img = os.path.join(_tarDir, u"ShareMedia/Images/auto1.png")

    @classmethod
    def cvShow(cls):
        import cv2
        lImgObj = cv2.imread(cls._cut0Img)
        imgR, imgG, imgB = cv2.split(lImgObj)


        cv2.imshow("R",imgR)
        cv2.imshow("G",imgG)
        cv2.imshow("B",imgB)
        cv2.waitKey(10)

    @classmethod
    def pltShow(cls):
        pass





if __name__ == "__main__":
    MainRun.cvShow()