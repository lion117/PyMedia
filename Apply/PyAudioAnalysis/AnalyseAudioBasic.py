# -*- coding: utf-8 -*-

import sys, os, time
import cv2, numpy
import logging

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
    def testDrawAllAudioFrame(cls):
        pass

    @classmethod
    def testDrawOneAudioFrame(cls):
        pass


if __name__ == "__main__":
    MainRun.runTest()