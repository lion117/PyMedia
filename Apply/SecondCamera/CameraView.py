# -*- coding: utf-8 -*-

import sys, os, time
import cv2
import  numpy

class MainRun():

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def runOpenBinar(cls):
        lCap = cv2.VideoCapture(3)
        if lCap.isOpened() is False:
            print(u"camera is not opened")
            return
        lCap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        lCap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        # lCap.set(cv2.CAP_PROP_FPS, 20)
        # lCap.set(cv2.CAP_PROP_FORMAT,  cv2.VideoWriter.fourcc('M','J','P','G'))
        with open("test.rgb","w") as lFile:
            while(True):
                lRet , lFrame = lCap.read()
                if lRet is True:

                    lRgba = cv2.cvtColor(lFrame,cv2.COLOR_BGR2RGBA)
                    cv2.imshow("img", lRgba)
                    # lByry = numpy.array(lRgba).reshape((3,4),dtype= numpy.int8)
                    # lFile.write(numpy.array(lRgba,dtype=numpy.uint8).ctypes)
                    lFile.write(numpy.array(lRgba,dtype=numpy.uint8).tobytes())

                    # numpy.array(lRgba).tofile("filename.rgba")

                    if cv2.waitKey(33) > -1:
                        break


        lCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    MainRun.runTest()
    MainRun.runOpenBinar()