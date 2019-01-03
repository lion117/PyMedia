# -*- coding: utf-8 -*-

import sys, os, time
import cv2

class MainRun():
    lImgDir = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/video")
    _video1 = os.path.join(lImgDir,u"test1.mp4")


    @staticmethod
    def testOpenCamera():
        lCap = cv2.VideoCapture(0)
        lCap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
        lCap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
        if lCap.isOpened() is False:
            print(u"open camera failed")
            return

        while True:
            lRet , lFrame = lCap.read()
            cv2.imshow("video", lFrame)
            if cv2.waitKey(1) > -1:
                break

        lCap.release()
        cv2.destroyAllWindows()


        pass

    @classmethod
    def testOpenVideo(cls):
        lCap = cv2.VideoCapture(cls._video1,cv2.CAP_FFMPEG )


        while True:
            lRet , lFrame = lCap.read()
            if lRet is False:
                break
            cv2.imshow("video", lFrame)
            if cv2.waitKey(66) > -1:
                break

        lCap.release()
        cv2.destroyAllWindows()


    @staticmethod
    def testSaveVideo():
        lCap = cv2.VideoCapture(0)
        if lCap.isOpened() is False:
            print(u"camera is not opened")
            return
        lCap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        lCap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        lCap.set(cv2.CAP_PROP_FPS,30)
        # lCodec = cv2.VideoWriter_fourcc(*'WMV2')
        # lWriter = cv2.VideoWriter('camp.wmv', lCodec,30,(1280,720))
        lCodec = cv2.VideoWriter_fourcc(*'WMV2')
        lWriter = cv2.VideoWriter('camp.wmv', lCodec,30,(1280,720))
        while True:
            lRet , lFrame = lCap.read()
            if lRet is False:
                break
            lWriter.write(lFrame)
            cv2.imshow('test',lFrame)
            if cv2.waitKey(33) > -1:
                break

        lCap.release()
        lWriter.release()
        cv2.destroyAllWindows()

        pass





if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.testOpenCamera()
    # MainRun.testOpenVideo()
    MainRun.testSaveVideo()