# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
gLogger = logging.getLogger(__name__)


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _audio = os.path.join(_tarDir, u"ShareMedia/Audio/count.wav")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")

    @classmethod
    def testChroma(cls):
        lFrameFile = os.path.join(os.getcwd(), "firstFrame.pcm")
        [Fs, x] = audioBasicIO.readAudioFile(lFrameFile)
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        # plt.subplot(2,1,1)

        # plt.subplot(2,1,2); plt.plot(F[1]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()
        lIndex = 9
        plt.plot(F[0][lIndex])
        plt.xlabel('Frame no')
        plt.ylabel(F[1][lIndex])
        plt.show()

if __name__ == "__main__":
    # MainRun.runTest()
    MainRun.testChroma()
    # a = numpy.array([1,2,3,4,5,6,7,8]).reshape([-1,2])
    # b = a[:,0]
    # print(a)
    # print(b)
    # numpy.fft.rfft()

