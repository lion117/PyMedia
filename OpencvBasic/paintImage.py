# -*- coding: utf-8 -*-

import sys, os, time
import cv2

class MainRun():
    lImgDir = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/video")
    _video1 = os.path.join(lImgDir,u"test1.mp4")




    @classmethod
    def testPaintVideo(cls):
        lCap = cv2.VideoCapture(cls._video1,cv2.CAP_FFMPEG )
        while True:
            lRet , lFrame = lCap.read()
            if lRet is False:
                break
            lFrame = MainRun.testPaintLine(lFrame)
            lFrame = MainRun.testPaintRectangle(lFrame)
            lFrame = MainRun.testPaintCircle(lFrame)
            lFrame = MainRun.testPaintText(lFrame)

            cv2.imshow("video", lFrame)
            if cv2.waitKey(66) > -1:
                break
        lCap.release()
        cv2.destroyAllWindows()


    @classmethod
    def testPaintLine(cls, tImg):
        cv2.line(tImg,(0,0),(640,480),(0,255,0))
        return  tImg

    @classmethod
    def testPaintRectangle(cls,tImg):
        cv2.rectangle(tImg,(0,0),(640,480),(0,255,0),2)
        return  tImg


    @classmethod
    def testPaintCircle(cls,tImg):
        cv2.circle(tImg,(100,100),20,(0,255,0),-1)
        return  tImg

    @classmethod
    def testPaintText(cls, tImg):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(tImg,'OpenCV',(10,200), font, 4,(255,255,255),2,cv2.LINE_AA)
        return  tImg



if __name__ == "__main__":
    print(os.getcwd())
    MainRun.testPaintVideo()