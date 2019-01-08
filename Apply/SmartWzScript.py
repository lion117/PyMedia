# -*- coding: utf-8 -*-

import sys, os, time
sys.path.insert(0,os.path.dirname(os.getcwd()))

import PIL.Image

import  AndroidOpt
import image.ImageDealing
import image.ImageMatch
from  image.SiftMatch import isFindTargetImage, findMatchImgXY


class Main():
    @classmethod
    def run(cls):
        lTartget = u"feature0.png"
        lScreenShoot = u"screenshot.png"
        # lTargetList = [u"feature0.png" , u"feature1.png",u"feature3.png",u"feature4.png",u"feature5.png"]
        lTargetList = [u"feature0.png" ,u"feature3.png",u"feature4.png",u"feature5.png"]

        lIndex = 0
        print (u"begin")
        while True:
            AndroidOpt.screenShoot()
            if os.path.exists(lScreenShoot) is False:
                print(u"screen shoot error")
                break

            Main.rotate(lScreenShoot)

            lRet, lx, ly = False, 0 ,0


            for itor in lTargetList:
                (lRet, lx, ly)  = findMatchImgXY(itor,lScreenShoot)
                if lRet is False:
                    time.sleep(1)
                    print (u"current times %d  skip diff "%( lIndex))
                    continue
                else:
                    AndroidOpt.tapScreen(lx, ly)
                    time.sleep(2)
                lIndex +=1
                print (u" %d Times"%(lIndex))

        print (u"done %d"%(lIndex))



    @staticmethod
    def rotate(tBigImg):
        lImge =  image.ImageDealing.imageRotateByPil(tBigImg)
        lImge.save(tBigImg)




if __name__ == "__main__":
    print os.getcwd()
    Main.run()