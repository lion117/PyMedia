# -*- coding: utf-8 -*-

import sys, os, time


import os
from PIL import Image
from enum import Enum

class OptImg(Enum):
    horizontal = 0
    vertical  =1




def imageJiont(tImageList, opt):#opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num=len(tImageList)
    lTempImg = Image.open(tImageList[0])
    width ,height= lTempImg.size
    if opt== OptImg.horizontal:
        new_img=Image.new('RGB',(image_num*width,height),255)
    else:
        new_img=Image.new('RGB',(width,image_num*height),255)

    x=y=0
    count=0
    for itorPath in tImageList:
        itorImg = Image.open(itorPath)
        new_img.paste(itorImg,(x,y))
        count+=1
        if opt==OptImg.horizontal:
            x+=width
        else :
            y+=height
    return new_img.point()









class MainTest():
    @staticmethod
    def testImageJiont():
        lList = [u"test1.jpg", u"test2.jpg"]
        lImge = imageJiont(lList, OptImg.vertical)
        lImge.show()


if __name__ == "__main__":
    print os.getcwd()
    MainTest.testImageJiont()