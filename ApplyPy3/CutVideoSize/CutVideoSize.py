# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
import VideoLib.SaveVideo

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
gLogger = logging.getLogger(__name__)


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _video = os.path.join(_tarDir, u"ShareMedia/video/phone_1080p_demo.mp4")
    _videoShow = os.path.join(_tarDir, u"ShareMedia/video/videoShow_1080p_8mins.mp4")
    _imageDemo  = os.path.join(_tarDir, u"ShareMedia/Images/girl720p.png")
    _yTop = 1.0/8
    _yButton = 5.0/8
    _xLeft  = 0
    _xRight = 1

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")

    @classmethod
    def CutImage(cls,tFrame, tleftPer, trightPer, ttopPer, tbuttonPer):
        lSrcHeight, lSrcWidth, lBit = tFrame.shape
        lXleft  =  int(lSrcWidth * tleftPer)
        lXright = int(lSrcWidth* trightPer)
        lYtop = int(lSrcHeight * ttopPer)
        lYbutton = int(lSrcHeight * tbuttonPer)
        lDestImg = tFrame[lYtop: lYbutton, lXleft: lXright]

        lText = str.format("xleft:%d, xright:%d,ytop:%d, ybutton:%d" % (lXleft,lXright,lYtop,lYbutton))
        gLogger.debug("image width:%d, height:%d"%(lSrcWidth,lSrcHeight))
        gLogger.debug(lText)
        lDestImg = cv2.putText(lDestImg, lText, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        lDstWidth  =  lXright  - lXleft
        lDstHeight  = lYbutton - lYtop
        return (lDestImg , lDstWidth ,lDstHeight)




    @classmethod
    def testCutImage(cls):
        lImgObj = cv2.imread(cls._imageDemo)
        lDstImg,lX,lH = MainRun.CutImage(lImgObj, cls._xLeft,cls._xRight,cls._yTop,cls._yButton)

        cv2.imshow("src", lImgObj)
        cv2.imshow("dst",lDstImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    @classmethod
    def testVideoCut(cls):
        lVHandle = cv2.VideoCapture(cls._video, cv2.CAP_FFMPEG)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            lFrame= cv2.rotate(lFrame,cv2.ROTATE_90_CLOCKWISE)
            lDstFrame,lW, lH = MainRun.CutImage(lFrame, cls._xLeft, cls._xRight,cls._yTop , cls._yButton)
            lMinRate  = 0.8
            lScope = cv2.resize(lDstFrame, (int(lW*lMinRate), int(lH*lMinRate)))
            cv2.imshow('video', lScope)
            if cv2.waitKey(18) > -1:
                break
        cv2.release()
        cv2.destroyAllWindows()
        pass

    @classmethod
    def testVideoConvert(cls):
        lVideoWriter  = None
        lVHandle = cv2.VideoCapture(cls._video, cv2.CAP_FFMPEG)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break

            lDstFrame, lW, lH = MainRun.CutImage(lFrame, cls._xLeft, cls._xRight, cls._yTop, cls._yButton)
            if lVideoWriter is None :
                gLogger.info("init video writer width:%d, height:%d"%(lW,lH))
                lFileName = "test1.wmv"
                lVideoWriter = VideoLib.SaveVideo.SaveVideoMgr(lW,lH,lFileName,50)

            lVideoWriter.write(lDstFrame)

        gLogger.info("finish video cut process")
        lVideoWriter.close()

    @classmethod
    def videoScope(cls, tXLeft, tXRight,tYTop,tYBotton,tSrcFile, tDstFile,tFrameRate):
        gLogger.info("[videoScop] begin video %s, xl:%0.2f,xr:%0.2f,yt:%0.2f,yb:%0.2f"%(tSrcFile,tXLeft,tXRight,tYTop,tYBotton))
        lVideoWriter = None
        lVHandle = cv2.VideoCapture(tSrcFile, cv2.CAP_FFMPEG)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            lDstFrame, lW, lH = MainRun.CutImage(lFrame, tXLeft, tXRight, tYTop, tYBotton)
            if lVideoWriter is None:
                gLogger.info("[videoScop] init video writer width:%d, height:%d" % (lW, lH))
                lVideoWriter = VideoLib.SaveVideo.SaveVideoMgr(lW, lH, tDstFile, tFrameRate)
            lVideoWriter.write(lDstFrame)

        gLogger.info("[videoScop] finish video cut process")
        lVideoWriter.close()

    @classmethod
    def videoScopeRotate(cls, tXLeft, tXRight, tYTop, tYBotton, tSrcFile, tDstFile, tFrameRate):
        gLogger.info("[videoScop] begin video %s, xl:%0.2f,xr:%0.2f,yt:%0.2f,yb:%0.2f" % (
        tSrcFile, tXLeft, tXRight, tYTop, tYBotton))
        lVideoWriter = None
        lVHandle = cv2.VideoCapture(tSrcFile, cv2.CAP_FFMPEG)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            lFrame= cv2.rotate(lFrame,cv2.ROTATE_90_CLOCKWISE)
            lDstFrame, lW, lH = MainRun.CutImage(lFrame, tXLeft, tXRight, tYTop, tYBotton)
            if lVideoWriter is None:
                gLogger.info("[videoScop] init video writer width:%d, height:%d" % (lW, lH))
                lVideoWriter = VideoLib.SaveVideo.SaveVideoMgr(lW, lH, tDstFile, tFrameRate)
            lVideoWriter.write(lDstFrame)

        gLogger.info("[videoScop] finish video cut process")
        lVideoWriter.close()

    @classmethod
    def testVideoBatProcess(cls):
        lList = []
        # lList.append((0,      1,        0,      0.55))
        # lList.append((0.05,   0.95,     0,      0.55))
        # lList.append((0.1,    0.9,      0,      0.55))
        # lList.append((0.15,   0.85,     0,      0.55))
        # lList.append((0.2,    0.8,      0,      0.55))
        # lList.append((0.25,   0.75,     0,      0.55))


        # lList.append((0,    1,      0.05,   0.55))
        # lList.append((0.05, 0.95,   0.05,   0.55))
        # lList.append((0.1,  0.9,    0.05,   0.55))
        # lList.append((0.15, 0.85,   0.05,   0.55))
        # lList.append((0.2,  0.8,    0.05,   0.55))
        # lList.append((0.25, 0.75,   0.05,   0.55))


        lList.append((0,    1,      0.1,   0.55))
        lList.append((0.05, 0.95,   0.1,   0.55))
        lList.append((0.1,  0.9,    0.1,   0.55))
        lList.append((0.15, 0.85,   0.1,   0.55))
        lList.append((0.2,  0.8,    0.1,   0.55))
        lList.append((0.25, 0.75,   0.1,   0.55))
        #
        #
        lList.append((0,    1,      0.15,   0.55))
        lList.append((0.05, 0.95,   0.15,   0.55))
        lList.append((0.1,  0.9,    0.15,   0.55))
        lList.append((0.15, 0.85,   0.15,   0.55))
        lList.append((0.2,  0.8,    0.15,   0.55))
        lList.append((0.25, 0.75,   0.15,   0.55))

        for itor in lList:

            lDstFile =  str.format("cutFile_%0.2f_%0.2f_%0.2f_%0.2f.wmv"%(itor[0],itor[1],itor[2],itor[3]))
            MainRun.videoScope(itor[0],itor[1],itor[2],itor[3],cls._videoShow,lDstFile,50)




    @classmethod
    def testVideoConvertForMp4(cls):
        lvideo = os.path.join(os.getcwd(),u"ayouyou.mp4")
        lVideoWriter  = None
        lVHandle = cv2.VideoCapture(lvideo, cv2.CAP_FFMPEG)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            lFrame= cv2.rotate(lFrame,cv2.ROTATE_90_CLOCKWISE)
            lDstFrame, lW, lH = MainRun.CutImage(lFrame, cls._xLeft, cls._xRight, cls._yTop, cls._yButton)
            if lVideoWriter is None :
                gLogger.info("init video writer width:%d, height:%d"%(lW,lH))
                lFileName = "ayouyou-90-cut.mp4"
                lVideoWriter = VideoLib.SaveVideo.SaveVideoMgr(lW,lH,lFileName,50)

            lVideoWriter.write(lDstFrame)

        gLogger.info("finish video cut process")
        lVideoWriter.close()

    @classmethod
    def testVideoBatRotate(cls):
        lListVideo = []
        # lListVideo.append("ayouyou.mp4")
        # lListVideo.append("guxiaojie.mp4")
        lListVideo.append("baijiajun.mp4")
        lListVideo.append("chengxuexun.mp4")
        lListVideo.append("dahuang.mp4")
        lListVideo.append("wangjinjin.mp4")
        lListVideo.append("xicheng.mp4")



        lCutPerCent  =(0,    1,      0.15,   0.55)
        for itor in lListVideo:
            lDstFile =  str.format("out_%s.mp4"%(itor))
            MainRun.videoScopeRotate(lCutPerCent[0],lCutPerCent[1],lCutPerCent[2],lCutPerCent[3],itor,lDstFile,50)



if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.testCutImage()
    # MainRun.testVideoCut()
    # MainRun.testVideoConvert()
    # MainRun.testVideoBatProcess()
    # MainRun.testVideoConvertForMp4()
    MainRun.testVideoBatRotate()