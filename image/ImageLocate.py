# -*- coding: utf-8 -*-

import sys, os, time

import cv2
import numpy as np


def filterMatches(kp1, kp2, matches, ratio = 0.8):#https://www.zhihu.com/question/23371175
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs


def isImageLocateBySIFT(tImgFirst, tImgSecond):
    lSiftHandle= cv2.xfeatures2d.SIFT_create()
    lBfHandle = cv2.BFMatcher(cv2.NORM_L2)


    kp1,des1 = lSiftHandle.detectAndCompute(tImgFirst, None)
    kp2,des2 = lSiftHandle.detectAndCompute(tImgSecond, None)
    #print 'kp2',kp2
    if kp2 == []:
        print('kp2 does not have the keypoint')
        return
    matches = lBfHandle.knnMatch(des1, des2, k=2)#KNNMatch，可设置K = 2 ，即对每个匹配返回两个最近邻描述符，仅当第一个匹配与第二个匹配之间的距离足够小时，才认为这是一个匹配。
    #print matches
    print ('kp1:',len(kp1))
    print( 'kp1:',len(kp2))
    p1,p2,kp_pairs = filterMatches(kp1, kp2, matches)
    print( "matches",len(kp_pairs))
    ratio = 0
    if min(len(kp1),len(kp2)):
        #ratio = (100*len(kp_pairs)/max(len(kp1),len(kp2)))
        ratio = (100*len(kp_pairs)/len(kp1))
    else:
        print("can't find SIFT point.")
    print ('lSiftHandle match ratio--------->%.2f%%'%ratio)
    return ratio


class MainTest():
    @staticmethod
    def testLocateImage():
        lSrc = u"game.png"
        lTarget  = u"game.png"
        lSrcImg = cv2.imread(lSrc,cv2.IMREAD_GRAYSCALE )
        lTargetImg = cv2.imread(lSrc,cv2.IMREAD_GRAYSCALE )
        lDiffValue =  isImageLocateBySIFT(lSrcImg, lTargetImg)
        print lDiffValue


if __name__ == "__main__":
    print os.getcwd()
    MainTest.testLocateImage()