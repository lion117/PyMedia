# -*- coding: utf-8 -*-

import sys, os, time
lParentDir = os.path.dirname(os.getcwd())
sys.path.insert(0,lParentDir)

import PIL.Image

import  AndroidOpt
import image.ImageDealing
import image.ImageMatch
from  image.SiftMatch import isFindTargetImage, findMatchImgXY

class Main():
    @staticmethod
    def run():
        lTartget = u"feature0.png"
        lJumpImg = u"skip.png"
        lScreenShoot = u"screenshot.png"
        lIndex = 0
        print (u"begin")
        while True:
            AndroidOpt.screenShoot()
            if os.path.exists(lScreenShoot) is False:
                print(u"screen shoot error")
                break


            Main.rotate(lScreenShoot)
            (lRet, lx, ly)  = findMatchImgXY(lTartget,lScreenShoot)
            if lRet is False:
                (lRet1, lx1, ly1)  = findMatchImgXY(lJumpImg,lScreenShoot)
                if lRet1 is False:
                    time.sleep(2)
                    print (u"current times %d  not found target image "%( lIndex))
                    continue
                else:
                    AndroidOpt.tapScreen(lx1, ly1)
                    print (u"current times %d  skip button "%( lIndex))
                    time.sleep(10)
                    continue
            else:
                AndroidOpt.tapScreen(lx, ly)
                time.sleep(2)
                lIndex +=1
                print (u" %d Times"%(lIndex))

        print (u"done %d"%(lIndex))

    @staticmethod
    def isStucked(tBigImg):
        lFeature0 = u"feature0.png"
        lFeature1 = u"feature1.png"
        if isFindTargetImage(lFeature0, tBigImg) is False:
            print (u"did not found the feature0 ")
            return False
        if isFindTargetImage(lFeature1 , tBigImg) is False:
            print (u"did not found the feature1 ")
            return False
        return  True

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
