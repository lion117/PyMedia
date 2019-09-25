# -*- coding: utf-8 -*-

import sys, os, time
import  cv2
import  Queue
from VideoLib.SaveVideo import SaveVideoMgr





class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")
    @classmethod
    def test(cls):
        lImg = cv2.imread(cls._img)
        cv2.imshow('test', lImg)
        cv2.waitKey(0)
        cv2.release()
        cv2.destroyAllWindows()

    @classmethod
    def testCut(cls):
        lImg = cv2.imread(cls._img)
        lPartImg = lImg[200:300,630:800]
        cv2.imshow('origin', lImg)
        cv2.imshow('cut', lPartImg)
        cv2.waitKey(0)
        cv2.release()
        cv2.destroyAllWindows()

    @classmethod
    def testWebm(cls):
        lVideo = os.path.join(cls._tarDir, u"ShareMedia/video/Japanin8K.webm")
        lVideo1 = os.path.join(cls._tarDir, u"ShareMedia/video/test1.mp4")
        lVHandle = cv2.VideoCapture(lVideo,cv2.CAP_FFMPEG)
        while True:

            lRet ,lFrame = lVHandle.read()
            if lRet is False:
                break
            lScope = cv2.resize(lFrame,(1280,720))
            cv2.imshow('8k', lScope)

            if cv2.waitKey(33) > -1:
                break
        cv2.release()
        cv2.destroyAllWindows()


class FilmScope():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    # _video8k = os.path.join(_tarDir, u"ShareMedia/video/Japanin8K.webm")
    _video8k = os.path.join(_tarDir, u"ShareMedia/video/DellPeople8K.webm")
    _effectQueue = Queue.Queue()
    _font = cv2.FONT_HERSHEY_SIMPLEX
    _width = 960
    _height = 540
    _effectType = -1
    _videoCounts  = 0
    _videoIndex  = -1
    _vWriter = SaveVideoMgr(_width,_height, os.path.join(os.getcwd(),"movie.wmv"),25)

    @classmethod
    def showVideo(cls):
        lVHandle = cv2.VideoCapture(cls._video8k, cv2.CAP_FFMPEG)
        lIndex = 0
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            lScope = cls.addFilmEffect(lFrame)
            cls._vWriter.write(lScope)
            # cv2.imshow('720p',lScope)
            # cv2.imshow('8k', cv2.resize(lFrame,(cls._width,cls._height)))
            if cv2.waitKey(1) > -1:
                break
            print("video frame index %d"%(lIndex))
            lIndex +=1

        cls._vWriter.close()
        # cv2.release()
        # cv2.destroyAllWindows()

    @classmethod
    def addEffect(cls, tEffectType, tTime):
        cls._effectQueue.put((tEffectType, tTime))

    @classmethod
    def addFilmEffect(cls, tSrcFrame):
        if cls._effectQueue.empty() and cls._effectType == -1:
            lDestFrame = cls.videoEffect(tSrcFrame,0,0)
            return  lDestFrame
        if cls._effectType  ==  -1:
            lItem = cls._effectQueue.get()
            cls._effectType = lItem[0]
            cls._videoCounts = lItem[1]*25
            cls._videoIndex = 0

        lDestFrame = cls.videoEffect(tSrcFrame , cls._effectType ,cls._videoCounts,cls._videoIndex)

        cls._videoIndex +=1
        if cls._videoIndex >= cls._videoCounts:
            cls._effectType = -1
            cls._videoCounts = 0
            cls._videoIndex = -1

        return  lDestFrame



    @classmethod
    def videoEffect(cls, tSrcFrame,tType, tCount, tIndex = 0):
        if tType == 0:
            lScope = cv2.resize(tSrcFrame, (cls._width, cls._height))
            lScope = cv2.putText(lScope, "type: 0  scope image",(50,50), cls._font, 1, (0,255,0))
            return  lScope

        if tType  == 1:
            lSrcHeight , lSrcWidth , lRet  = tSrcFrame.shape
            lCentX , lCentY = (lSrcWidth /2 , lSrcHeight/2)
            lLeftX , lLeftY = (lCentX  - cls._width/2 , lCentY - cls._height/2)
            lRightX , lRightY = (lCentX  + cls._width/2 , lCentY + cls._height/2)
            lScope = tSrcFrame[ lLeftY : lRightY,lLeftX: lRightX ]
            lScope = cv2.putText(lScope, "type: 1 cut image",(50,50), cls._font, 1, (0,255,0))
            return  lScope

        if tType == 2:
            if tCount == 0 or tCount < tIndex:
                print("invalid para")
                return  tSrcFrame
            lSrcHeight , lSrcWidth , lRet  = tSrcFrame.shape
            lCentX , lCentY = (lSrcWidth /2 , lSrcHeight/2)
            lLeftX , lLeftY = (lCentX  - cls._width/2 , lCentY - cls._height/2)
            lRightX , lRightY = (lCentX  + cls._width/2 , lCentY + cls._height/2)
            lUnitX , lUnitY = (lLeftX / tCount , lLeftY / tCount)
            lIncrX , lIncrY = lUnitX * (tCount - tIndex) , lUnitY * (tCount - tIndex)
            lRealLeftX  , lRealLeftY = lLeftX - lIncrX , lLeftY - lIncrY
            lRealRightX , lRealRightY = lRightX + lIncrX , lRightY + lIncrY

            lScope = tSrcFrame[ lRealLeftY : lRealRightY,lRealLeftX: lRealRightX ]
            lScope  = cv2.resize(lScope, (cls._width, cls._height))
            lScope = cv2.putText(lScope, "type: 2 scope MIN image",(50,50), cls._font, 1, (0,255,0))
            return  lScope

        if tType == 3:
            if tCount == 0 or tCount < tIndex:
                print("invalid para")
                return tSrcFrame
            lSrcHeight, lSrcWidth, lRet = tSrcFrame.shape
            lCentX, lCentY = (lSrcWidth / 2, lSrcHeight / 2)
            lLeftX, lLeftY = (lCentX - cls._width / 2, lCentY - cls._height / 2)
            lRightX, lRightY = (lCentX + cls._width / 2, lCentY + cls._height / 2)
            lUnitX, lUnitY = (lLeftX / tCount, lLeftY / tCount)
            lIncrX, lIncrY = lUnitX * ( tIndex), lUnitY * (tIndex)
            lRealLeftX, lRealLeftY = lLeftX - lIncrX, lLeftY - lIncrY
            lRealRightX, lRealRightY = lRightX + lIncrX, lRightY + lIncrY

            lScope = tSrcFrame[lRealLeftY: lRealRightY, lRealLeftX: lRealRightX]
            lScope = cv2.resize(lScope, (cls._width, cls._height))
            lScope = cv2.putText(lScope, "type: 2 scope MAX image", (50, 50), cls._font, 1, (0, 255, 0))
            return lScope







if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.test()
    # MainRun.testCut()
    # MainRun.testWebm()
    FilmScope.addEffect(0,10)
    FilmScope.addEffect(2,10)
    FilmScope.addEffect(3,10)
    FilmScope.addEffect(0,10)
    FilmScope.addEffect(2,10)
    FilmScope.addEffect(3,10)
    FilmScope.showVideo()