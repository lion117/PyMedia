# -*- coding: utf-8 -*-

import sys, os, time


class MainRun():
    _rgbSrc =os.path.join(os.getcwd() , u"src.rgb")
    _rgbDst =os.path.join(os.getcwd() , u"dst.rgb")


    @classmethod
    def runTest(cls):
        print(u"hello world")





if __name__ == "__main__":
    MainRun.runTest()