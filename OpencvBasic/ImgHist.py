# -*- coding: utf-8 -*-

import sys, os, time



from matplotlib import pyplot as plt
import numpy as np
import cv2



class MainRun():
    lPic0 = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/Images/auto0.png")
    lPic1 = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/Images/auto1.png")


    @classmethod
    def runDemo(cls):
        image = cv2.imread(cls.lPic1)
        cv2.imshow("Original",image)
        #cv2.waitKey(0)

        chans = cv2.split(image)
        colors = ("b","g","r")
        plt.figure()
        plt.title("Flattened Color Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")

        for (chan,color) in zip(chans,colors):
            hist = cv2.calcHist([chan],[0],None,[256],[0,256])
            plt.plot(hist,color = color)
            plt.xlim([0,256])
        plt.show()


if __name__ == "__main__":
    MainRun.runDemo()