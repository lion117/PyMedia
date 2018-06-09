# -*- coding: utf-8 -*-

import sys, os, time
import  AndroidOpt
import image.ImageMatch
from  image.SiftMatch import isFindTargetImage, findMatchImgXY


class Main():
    @staticmethod
    def run():
        lTartget = u"feature0.png"
        lScreenShoot = u"screenshot.png"
        lIndex = 0
        print (u"begin")
        while True:
            AndroidOpt.screenShoot()
            if os.path.exists(lScreenShoot) is False:
                print(u"screen shoot error")
                break

            # if  Main.isStucked(lScreenShoot) is False:
            #     time.sleep(2)
            #     continue

            (lRet, lx, ly)  = findMatchImgXY(lTartget,lScreenShoot)
            print lRet, lx, ly
            # (lRet , lValue)= image.ImageMatch.isImageDiffMuch(lScreenShoot, lTemplate)
            # if lRet is True:
            #     time.sleep(2)
            #     print (u"current times %d  skip diff value %d    "%( lIndex,lValue))
            #     continue
            # else:
            #     AndroidOpt.clickScreen()
            #     time.sleep(2)
            # lIndex +=1
            # print (u" %d Times"%(lIndex))

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




class MainTest():
    @staticmethod
    def testPrint():
        pass

if __name__ == "__main__":
    print os.getcwd()
    Main.run()