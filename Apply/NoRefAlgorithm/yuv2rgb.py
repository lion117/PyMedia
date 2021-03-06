# -*- coding: utf-8 -*-

import sys, os, time


class MainRun():

    @classmethod
    def runTest(cls):
        print(u"hello world")



import cv2
from numpy import *

screenLevels = 255.0
def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    blk_size = prod(dims) *3/2
    fp.seek(blk_size*startfrm,0)
    Y=[]
    U=[]
    V=[]
    print dims[0]
    print dims[1]
    d00=dims[0]//2
    d01=dims[1]//2
    print d00
    print d01
    Yt=zeros((dims[0],dims[1]),uint8,'C')
    Ut=zeros((d00,d01),uint8,'C')
    Vt=zeros((d00,d01),uint8,'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                #print m,n
                Yt[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Vt[m,n]=ord(fp.read(1))
        Y=Y+[Yt]
        U=U+[Ut]
        V=V+[Vt]
    fp.close()
    return [Y,U,V]


if __name__ == '__main__':
    width=1280
    height=720
    data=yuv_import('1280x720_6.yuv',(height,width),1,0)
    YY=data[0][0]
    cv2.imshow("yuv420",YY)
    cv2.waitKey(0)


