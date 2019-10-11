# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
import scipy.io.wavfile
import matplotlib.pyplot as plt
import math

gLogger = logging.getLogger("pylog")
gLogger.setLevel(logging.DEBUG)
rf_handler = logging.StreamHandler(sys.stderr)#默认是sys.stderr
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('pylog.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

gLogger.addHandler(rf_handler)
gLogger.addHandler(f_handler)


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")
    _song = os.path.join(_tarDir, u"ShareMedia/Audio/xiaoqingge.wav")
    _audioStep = 0.01
    _audioWindows  = 0.025

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")


    @classmethod
    def testNumpy(cls):
        lMatrix1 = numpy.ones((1,8))
        print(lMatrix1)
        lMatrix2 = lMatrix1.reshape((2,4))
        print(lMatrix2)

    @classmethod
    def testReadAudio(cls):
        lSigalRate,lSignal = scipy.io.wavfile.read(cls._song)
        gLogger.info("sigal rate:%d ,len:%d", lSigalRate, len(lSignal))


    @classmethod
    def testSplitPcmChannel(cls):
        lSigalRate,lSignal = scipy.io.wavfile.read(cls._song)
        gLogger.info("sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)


        lChannelLeft = lSignalMat[:,0]
        lChannelRight = lSignalMat[:,1]

        lSignalMat.tofile("lSignal.pcm")
        lChannelLeft.tofile("lChannelLeft.pcm")
        lChannelRight.tofile("lChannelRight.pcm")
        lBuff = lSignalMat.tostring()
        with open("rawAudio.pcm","wb+") as pcmFile:
            pcmFile.write(lBuff)

    @classmethod
    def testSpeedUpPcm(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._song)
        gLogger.info("sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)

        lChannelLeft = lSignalMat[:, 0]
        lChannelRight = lSignalMat[:, 1]
        gLogger.info(lChannelLeft.shape)
        tmp = numpy.reshape(lChannelRight[:-1], (-1, 2))
        gLogger.info(tmp.shape)
        tmp[:,0].tofile("halfaudio.pcm")

    @classmethod
    def testAudioWindowsFile(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._song)
        gLogger.info("sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)
        lChannelLeft = lSignalMat[:, 0]
        lChannelRight = lSignalMat[:, 1]
        gLogger.info(lChannelLeft.shape)

        lAudioWindow = int(math.floor(cls._audioWindows* lSigalRate))
        lAudioStepSize  = cls._audioStep * lSigalRate


        # lIndex  = lAudioWindow
        # lMergerMat  =  lChannelLeft[0:lAudioWindow]
        # while lIndex + lAudioWindow < len(lSignal)  :
        #     lMergerMat = numpy.vstack( (lMergerMat, lChannelLeft[lIndex:lIndex+lAudioWindow]))
        #     lIndex += lAudioWindow
        #
        # gLogger.info("finish merger stack")
        # lMergerMat.tofile("merget.pcm")

        lIndex = lAudioWindow
        lHamming = numpy.hamming(lAudioWindow)
        lMergerMat = lChannelLeft[0:lAudioWindow]
        lMergerMat = lMergerMat

        while lIndex + lAudioWindow < len(lSignal):
            lMergerMat = numpy.vstack((lMergerMat, lChannelLeft[lIndex:lIndex + lAudioWindow] ))
            lIndex += int(lAudioStepSize)        # 仅挪动步长

        gLogger.info("finish merger hamming stack")
        lMergerMat.tofile("mergeHamming.pcm")







    @classmethod
    def testAudioDrawFeature(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._song)
        gLogger.info("sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)
        lChannelLeft = lSignalMat[:, 0]
        lChannelRight = lSignalMat[:, 1]
        gLogger.info(lChannelLeft.shape)

        lAudioWindow = int(math.floor(cls._audioWindows * lSigalRate))
        lAudioStepSize = cls._audioStep * lSigalRate

        lFirstWindow = lChannelLeft[0:lAudioWindow]
        lHamming = numpy.hamming(lAudioWindow)
        lExFirstWindow = lFirstWindow * lHamming

        lFirstWindow.tofile("firstFrame.pcm")
        lExFirstWindow.tofile("hammingFrame.pcm")

        plt.subplot(131)
        plt.plot(abs(numpy.fft.fft(lChannelLeft,lAudioWindow)))
        plt.subplot(132)
        plt.plot(abs((numpy.fft.fft(lFirstWindow))))
        plt.subplot(133)
        plt.plot(abs((numpy.fft.fft(lExFirstWindow,lAudioWindow))))
        plt.show()








if __name__ == "__main__":
    # MainRun.runTest()
    # MainRun.testNumpy()
    # MainRun.testReadAudio()
    # MainRun.testSplitPcmChannel()
    # MainRun.testSpeedUpPcm()
    # MainRun.testAudioWindowsFile()
    MainRun.testAudioDrawFeature()