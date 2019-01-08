# -*- coding: utf-8 -*-

import sys, os, time
import cv2
from matplotlib import  pyplot as plt


lParentDir = os.path.dirname(os.path.dirname(os.getcwd()))
lImageDir = os.path.join(lParentDir,u"ShareMedia/Images")
# sys.path.insert(0,lParentDir)


def GetImg(tFileName):
    lFile = os.path.join(lImageDir, tFileName)
    return  lFile




def matplotlib_multi_pic2():
    plt.gcf().canvas.set_window_title('Test')
    plt.gcf().suptitle("multi pic test")


    lFile1 = os.path.join(lImageDir,u"cat0.jpg")
    lFile2 = os.path.join(lImageDir,u"cat1.jpg")
    lFile3 = os.path.join(lImageDir,u"dog0.jpg")

    lImage1= cv2.imread(lFile1)
    lImage2 = cv2.imread(lFile2)
    lImage3 = cv2.imread(lFile3)

    lGray1 = cv2.cvtColor(lImage1,cv2.COLOR_RGB2BGR)
    lGray2 = cv2.cvtColor(lImage2,cv2.COLOR_RGB2BGR)
    lGray3 = cv2.cvtColor(lImage3,cv2.COLOR_RGB2BGR)
    lGray4 = cv2.cvtColor(lImage1,cv2.COLOR_RGB2GRAY)

    # 如果总图片个数不超过10，我们还可以用快速的方法
    plt.subplot(321), plt.imshow(lImage1), plt.title("1")
    plt.subplot(322), plt.imshow(lGray1,cmap="gray"), plt.title("1'")

    plt.subplot(323), plt.imshow(lImage2), plt.title("2")
    plt.subplot(324), plt.imshow(lGray2), plt.title("2'")

    plt.subplot(325), plt.imshow(lImage3), plt.title("3")
    plt.subplot(326), plt.imshow(lGray3), plt.title("3'")
    cv2.imshow("cv",lGray4)
    plt.show()





class MainTestRun():
    @staticmethod
    def runMatPlotMutlImage():
        matplotlib_multi_pic2()

if __name__ == "__main__":
    print(os.getcwd())
    MainTestRun.runMatPlotMutlImage()