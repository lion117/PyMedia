# -*- coding: utf-8 -*-

import sys, os, time


import os
from PIL import Image
from enum import Enum
import  numpy

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
    return new_img



def imageJiontByRaw(tImageList, tWidth , tHeight ,opt):
    image_num = len(tImageList)
    width, height = (tWidth , tHeight)
    if opt == OptImg.horizontal:
        new_img = Image.new('RGB', (image_num * width, height), 255)
    else:
        new_img = Image.new('RGB', (width, image_num * height), 255)

    x = y = 0
    count = 0
    for itor in tImageList:
        new_img.paste(itor, (x, y))
        count += 1
        if opt == OptImg.horizontal:
            x += width
        else:
            y += height
    return convertPilToCv2(new_img)


def convertPilToCv2(tImg):
    open_cv_image = numpy.array(tImg)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return  open_cv_image


class MainTest():
    @staticmethod
    def testImageJiont():
        lList = [u"test1.jpg", u"test2.jpg"]
        lImge = imageJiont(lList, OptImg.vertical)
        lImge.show()


if __name__ == "__main__":
    print os.getcwd()
    MainTest.testImageJiont()