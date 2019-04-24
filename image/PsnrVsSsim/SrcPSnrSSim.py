# -*- coding: utf-8 -*-

import sys, os, time
import  numpy
import  cv2

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img1 = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")
    _img2 = os.path.join(_tarDir, u"ShareMedia/Images/cat0_gray.jpg")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def psnr(cls, tImg1, tImg2):
        mse = (numpy.abs(tImg1 - tImg2) ** 2).mean()
        psnr = 10 * numpy.log10(255 * 255 / mse)
        return psnr

    @classmethod
    def ssim(cls, tImg1, tImg2):
        assert len(tImg1.shape) == 2 and len(tImg2.shape) == 2
        assert tImg1.shape == tImg2.shape
        mu1 = tImg1.mean()
        mu2 = tImg2.mean()
        sigma1 = numpy.sqrt(((tImg1 - mu1) ** 2).mean())
        sigma2 = numpy.sqrt(((tImg2 - mu2) ** 2).mean())
        sigma12 = ((tImg1 - mu1) * (tImg2 - mu2)).mean()
        k1, k2, L = 0.01, 0.03, 255
        C1 = (k1 * L) ** 2
        C2 = (k2 * L) ** 2
        C3 = C2 / 2
        l12 = (2 * mu1 * mu2 + C1) / (mu1 ** 2 + mu2 ** 2 + C1)
        c12 = (2 * sigma1 * sigma2 + C2) / (sigma1 ** 2 + sigma2 ** 2 + C2)
        s12 = (sigma12 + C3) / (sigma1 * sigma2 + C3)
        ssim = l12 * c12 * s12
        return ssim


    @classmethod
    def testPsnr(cls):
        lImg1 = cv2.imread(cls._img1)
        lImg2 = cv2.imread(cls._img2)
        cv2.imshow("im1",lImg1)
        cv2.imshow("im2",lImg2)


        lpsrn = MainRun.psnr(numpy.array(lImg1),numpy.array(lImg2))
        print(lpsrn)



    @classmethod
    def testSsim(cls):
        lImg1 = cv2.imread(cls._img1)
        lImg2 = cv2.imread(cls._img2)
        lssim = MainRun.ssim(lImg1,lImg2)
        print(lssim)



if __name__ == "__main__":
    MainRun.runTest()
    MainRun.testPsnr()
    # MainRun.testSsim()