# -*- coding: utf-8 -*-

import sys, os, time


# import numpy as np
# from skimage import exposure,data
# image =data.camera()*1.0
# hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
# hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
# print(hist1)
# print(hist2)
#
#
# from skimage import data
# import matplotlib.pyplot as plt
# img=data.camera()
# plt.figure("hist")
# arr=img.flatten()
# n, bins, patches = plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red')
# plt.show()


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def ConvertHist(tImage):
    if os.path.exists(tImage) is False:
        print(u"%s not found"%tImage)
        return
    img = np.array(Image.open(tImage).convert('L'))
    plt.figure('cat')
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)
    plt.show()




class MainTest():
    @staticmethod
    def testConvertHist():
        lImage = u"hongkong.jpg"
        ConvertHist(lImage)

if __name__ == "__main__":
    print os.getcwd()
    MainTest.testConvertHist()