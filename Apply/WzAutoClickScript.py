# -*- coding: utf-8 -*-

import sys, os, time
import  AndroidOpt
import  image.ImageMatch

class Main():
    @staticmethod
    def run():
        lTemplate = u"template.png"
        lScreenShoot = u"screenshot.png"
        lIndex = 0
        print (u"begin")
        while True:
            AndroidOpt.screenShoot()
            if os.path.exists(lScreenShoot) is False:
                print(u"screen shoot error")
                break

            (lRet , lValue)= image.ImageMatch.isImageDiffMuch(lScreenShoot, lTemplate)
            if lRet is True:
                time.sleep(2)
                printOnce (u"skip diff value %d  current times %d"%(lValue, lIndex))
                continue
            else:
                AndroidOpt.clickScreen()
                time.sleep(2)
            lIndex +=1
            printOnce (u" %d Times"%(lIndex))

        print (u"done %d"%(lIndex))


def printOnce(tInfo):
    print u"\r",
    print tInfo,


class MainTest():
    @staticmethod
    def testPrint():
        for i in range(100):
            printOnce(i)


if __name__ == "__main__":
    # print os.getcwd()
    Main.run()
    # MainTest.testPrint()