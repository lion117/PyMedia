# -*- coding: utf-8 -*-

import sys, os, time
import  numpy
import cv2
import matplotlib.pyplot as  plt

class MainRun():
    _rgbSrc =os.path.join(os.getcwd() , u"video/src1.rgb")
    _rgbDst =os.path.join(os.getcwd() , u"video/dst1.rgb")
    _width = 640
    _height = 480


    @classmethod
    def runTest(cls):
        print(u"hello world")


    @classmethod
    def readImg(cls, tFile, tWidth, tHeight,tIndex=0,tBytePerPix = 4):
        with open(tFile,"rb") as lFile:
            lFile.seek(tWidth*tHeight*tBytePerPix * tIndex)
            lBuff = lFile.read(tWidth*tHeight*tBytePerPix)
            lBuff = numpy.frombuffer(lBuff,dtype='uint8')
            lBuff = numpy.reshape(lBuff,(tHeight,tWidth,4))
            lImgInfo =  numpy.array(lBuff)
            # cv2.imshow("test",lImgInfo)
            # cv2.waitKey(10000)
            return  lImgInfo

    @classmethod
    def readRgb(cls):
        lRGBA = MainRun.readImg(cls._rgbSrc,cls._width, cls._height)
        lBGRAObj = cv2.cvtColor(numpy.array(lRGBA), cv2.COLOR_RGB2BGR)

        lB, lG, lR = cv2.split(lBGRAObj)
        lMean = cv2.mean(lR)[0]
        print(lMean)
        cv2.imshow("rgba",lBGRAObj)
        # hist= cv2.calcHist(lBGRAObj, [0], None, [256], [0.0,255.0])
        # cv2.imshow("R", hist)
        cv2.waitKey(20000)


    @classmethod
    def readV2(cls):
        lBuff = numpy.fromfile(cls._rgbSrc,dtype='uint8',count= cls._width* cls._height *4 )
        lBuff = numpy.reshape(lBuff,(cls._height,cls._width,4))
        lImgInfo =  numpy.array(lBuff)
        lBGRAObj = cv2.cvtColor(lImgInfo, cv2.COLOR_RGB2BGR)
        cv2.imshow("test",lBGRAObj)
        cv2.waitKey(10000)

    @classmethod
    def compareSrcDst(cls):
        lRGBASrc = MainRun.readImg(cls._rgbSrc, cls._width, cls._height)
        lRGBADst = MainRun.readImg(cls._rgbDst, cls._width, cls._height)
        lSrc = cv2.cvtColor(numpy.array(lRGBASrc), cv2.COLOR_RGB2BGR)
        lDst = cv2.cvtColor(numpy.array(lRGBADst), cv2.COLOR_RGB2BGR)

        lSrcB, lSrcG, lSrcR = cv2.split(lSrc)
        lDstB, lDstG, lDstR = cv2.split(lDst)

        lMeanSrc = cv2.mean(lSrcR)[0]
        lMeanDst = cv2.mean(lDstR)[0]
        print(u"src mean: %d , dst mean: %d, diff %d"%(lMeanSrc, lMeanDst, lMeanSrc-lMeanDst))
        MainRun.compareImg(lSrc,lDst,lSrcR,lDstR)


    @classmethod
    def compareImg(cls, tSrc, tDst, tSrcR, tDstR):

        plt.figure()
        plt.subplot(221) ,plt.imshow(tSrc)
        plt.subplot(222),plt.imshow(tDst)
        zeros = numpy.zeros((480,640,1),dtype="uint8")
        plt.subplot(223),plt.imshow(cv2.merge((tSrcR,zeros,zeros)) )
        plt.subplot(224),plt.imshow(cv2.merge((tDstR,zeros,zeros)))
        plt.show()

    @classmethod
    def compareVideoSrcDst(cls):
        for i in range(10):
            lRGBASrc = MainRun.readImg(cls._rgbSrc, cls._width, cls._height,i)
            lRGBADst = MainRun.readImg(cls._rgbDst, cls._width, cls._height,i)
            lSrc = cv2.cvtColor(numpy.array(lRGBASrc), cv2.COLOR_RGB2BGR)
            lDst = cv2.cvtColor(numpy.array(lRGBADst), cv2.COLOR_RGB2BGR)

            lSrcB, lSrcG, lSrcR = cv2.split(lSrc)
            lDstB, lDstG, lDstR = cv2.split(lDst)

            lMeanSrc = cv2.mean(lSrcR)[0]
            lMeanDst = cv2.mean(lDstR)[0]
            print(u"src mean: %d , dst mean: %d, diff %d tIndex %d" % (lMeanSrc, lMeanDst, lMeanSrc - lMeanDst, i))
            MainRun.compareImg(lSrc, lDst, lSrcR, lDstR)
            lwait = raw_input()



if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.readRgb()
    # MainRun.readV2()
    # MainRun.compareSrcDst()
    MainRun.compareVideoSrcDst()