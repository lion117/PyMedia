# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import scipy.io.wavfile



gLogger = logging.getLogger("pylog")
gLogger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)  #默认是sys.stderr
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
    _rawWav = os.path.join(_tarDir, u"ShareMedia/Audio/xiaoqinge_1channel.wav")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")


    @classmethod
    def runDemo(cls):
        [Fs, x] = audioBasicIO.readAudioFile(cls._rawWav)
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.025*Fs, 0.01*Fs)
        plt.subplot(211);plt.plot(F[0,:]);plt.xlabel("frame no");plt.ylabel("ZCR")
        plt.subplot(212);plt.plot(F[1,:]); plt.xlabel("frame no");plt.ylabel("energy")
        plt.show()


    @classmethod
    def runBasicFeature(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._rawWav)
        gLogger.info("load song sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)
        lSecondAudio  = lSignalMat[0:lSigalRate*1]
        gLogger.info("second audio len:%d", len(lSecondAudio))

        F = audioFeatureExtraction.stFeatureExtraction(lSecondAudio, lSigalRate, 0.025*lSigalRate, 0.01*lSigalRate)
        plt.subplot(211);plt.plot(F[0][0]);plt.xlabel("frame no");plt.ylabel("ZCR")
        plt.subplot(212);plt.plot(F[0][1]); plt.xlabel("frame no");plt.ylabel("energy")
        plt.show()

    @classmethod
    def runAudioAllFeature(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._rawWav)
        gLogger.info("load song sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)
        lSecondAudio  = lSignalMat[0:lSigalRate*1]
        gLogger.info("second audio len:%d", len(lSecondAudio))

        F = audioFeatureExtraction.stFeatureExtraction(lSecondAudio, lSigalRate, 0.025*lSigalRate, 0.01*lSigalRate)
        lMaxSize = 5

        for i in range(0,lMaxSize):
            plt.subplot(lMaxSize,1,i+1);plt.plot(F[0][i]);plt.xlabel("frame no");plt.ylabel(F[1][i])
        plt.show()

    @classmethod
    def runAudioSpecialFeature(cls):
        lSigalRate, lSignal = scipy.io.wavfile.read(cls._rawWav)
        gLogger.info("load song sigal rate:%d ,len:%d ", lSigalRate, len(lSignal))
        lSignalMat = numpy.array(lSignal)
        gLogger.info(lSignalMat.dtype)
        gLogger.info(lSignalMat.shape)
        lSecondAudio = lSignalMat[0:lSigalRate * 1]
        gLogger.info("second audio len:%d", len(lSecondAudio))

        F = audioFeatureExtraction.stFeatureExtraction(lSecondAudio, lSigalRate, 0.025 * lSigalRate, 0.01 * lSigalRate)

        lTargetList  = []
        lTargetList.append(3)
        lTargetList.append(4)
        lTargetList.append(5)

        lSize  = len(lTargetList)

        for lIndex , itor in enumerate(lTargetList):
            plt.subplot(lSize,1,lIndex+1);plt.plot(F[0][itor]);plt.xlabel("frame no");plt.ylabel(F[1][itor])
        # for lIndex , itor in zip(range(0,lSize),lTargetList):
        #     plt.subplot(lSize,1,lIndex+1);plt.plot(F[0][itor]);plt.xlabel("frame no");plt.ylabel(F[1][itor])
        #
        plt.show()



if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.runDemo()
    # MainRun.runBasicFeature()
    # MainRun.runAudioAllFeature()
    MainRun.runAudioSpecialFeature()