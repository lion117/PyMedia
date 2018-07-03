# -*- coding: utf-8 -*-

import sys, os, time
lParentDir = os.path.dirname(os.getcwd())
sys.path.insert(0,lParentDir)

import PIL.Image

import  AndroidOpt
import image.ImageDealing
import image.ImageMatch
from  image.SiftMatch import isFindTargetImage, findMatchImgXY

g_ticks =0

class Main():

    @staticmethod
    def run():
        global  g_ticks
        lTartget = u"feature0.png"
        lJumpImg = u"skip.png"
        lScreenShoot = u"screenshot.png"
        lIndex = 0
        print (u"begin")
        while True:
            g_ticks +=1
            Main.isTimeToKill(g_ticks)
            lDevice = Main.getAndroidDevice()
            AndroidOpt.screenShoot(tDevice=lDevice)
            if os.path.exists(lScreenShoot) is False:
                print(u"screen shoot error")
                break

            Main.rotate(lScreenShoot)
            (lRet, lx, ly)  = findMatchImgXY(lTartget,lScreenShoot)
            if lRet is False:
                (lRet1, lx1, ly1)  = findMatchImgXY(lJumpImg,lScreenShoot)
                if lRet1 is False:
                    time.sleep(2)
                    print (u"current times %d  not found target image device:%s "%( lIndex,lDevice))
                    continue
                else:
                    AndroidOpt.tapScreen(lx1, ly1,tDevice=lDevice)
                    print (u"current times %d  skip button device:%s "%( lIndex,lDevice))
                    time.sleep(10)
                    continue
            else:
                AndroidOpt.tapScreen(lx, ly,tDevice=lDevice)
                time.sleep(2)
                lIndex +=1
                print (u" %d Times device:%s"%(lIndex,lDevice))

        print (u"done %d"%(lIndex))

    @staticmethod
    def getAndroidDevice():
        lDvList = AndroidOpt.fetchEmulatorDevice()
        lSize = len(lDvList)
        if lSize <2:
            return None
        else:
            lIndex = g_ticks % lSize
            return lDvList[lIndex]

    @staticmethod
    def isTimeToKill(tIndex):
        lDvList = AndroidOpt.fetchEmulatorDevice()
        lSize = len(lDvList)
        if tIndex > 90*(lSize):
            for itor in lDvList:
                AndroidOpt.killWz(itor)

    @staticmethod
    def rotate(tBigImg):
        lImge =  image.ImageDealing.imageRotateByPil(tBigImg)
        lImge.save(tBigImg)


class MainTest():
    @staticmethod
    def testPrint():
        pass

if __name__ == "__main__":
    print os.getcwd()
    Main.run()
