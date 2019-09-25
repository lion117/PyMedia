# -*- coding: utf-8 -*-

import sys, os, time
import cv2


class MainRun():

    @classmethod
    def runTest(cls):
        print(u"hello world")


class SaveVideoMgr():
    def __init__(self, tW, tH, tDstFile,tFrameRate = 24):
        lCodec = cv2.VideoWriter_fourcc(*'WMV2')
        self.vWriter = cv2.VideoWriter(tDstFile, lCodec, 24, (tW, tH)) # wmv

    def write(self, tFrame):
        self.vWriter.write(tFrame)

    def close(self):
        self.vWriter.release()



if __name__ == "__main__":
    MainRun.runTest()