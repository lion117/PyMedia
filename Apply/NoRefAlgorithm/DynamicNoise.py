# -*- coding: utf-8 -*-

import sys, os, time
import  numpy as np
import cv2

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _rgba = os.path.join(_tarDir, u"ShareMedia/video/640x480_static.rgba")
    _width  = 640
    _height = 480

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def testMat(cls):
        # np.cov(np.vstack([i.ravel() for i in arrs]))
        arrays = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4] ])
        print(arrays)
        itemArr = np.vstack(arrays)
        print(itemArr)
        varArr = np.var(itemArr,axis=0,ddof=1)
        print(varArr)
        print(np.mean(varArr))
        pass

    @classmethod
    def testArraySum(cls, tArr):
        pass

    @classmethod
    def readRgba(cls, tFile, tWidth, tHeight, tBytePerPix=4):
        lImgArr = []
        lSize  = tWidth * tHeight * tBytePerPix
        with open(tFile, "rb") as lFile:
            lIndex = 0
            while True:
                lFile.seek(lSize * lIndex)
                lBuff = None
                lBuff = lFile.read(lSize)
                if lBuff is None or len(lBuff) != lSize:
                    break
                lIndex += 1
                lBuff = np.frombuffer(lBuff, dtype='uint8')
                lImgMat = np.reshape(lBuff, (tHeight, tWidth, 4))
                ImgY, ImgU, ImgV = cv2.split(cv2.cvtColor(lImgMat, cv2.COLOR_BGR2YCrCb))
                lImgArr.append(ImgV)
                if lIndex > 29:
                    break
        return lImgArr

    @classmethod
    def calculateNoisy(cls):
        lArrayImg = MainRun.readRgba(cls._rgba,cls._width, cls._height,4)
        lVarMat = np.var(np.vstack([i.ravel() for i in lArrayImg] ), ddof=1, axis=0)
        lMean = np.mean(lVarMat)
        print(lMean)
        return lMean



    @classmethod
    def testReadRgbaFile(cls):
        lArrayImg = MainRun.readRgba(cls._rgba,cls._width, cls._height,4)
        for itor in lArrayImg:
            cv2.imshow("rgba", itor)
            cv2.waitKey(1000)
        cv2.destroyAllWindows()

    @classmethod
    def testDataCamera(cls):
        lwidth = 960
        lheight = 720
        logicFile = os.path.join(cls._tarDir, u"ShareMedia/video/cameraData_logic.rgba")
        bdbaFile = os.path.join(cls._tarDir, u"ShareMedia/video/cameraData_bdba.rgba")

        lArrayImgLogic = MainRun.readRgba(logicFile, lwidth, lheight, 4)
        lVarMatLogic = np.var(np.vstack([i.ravel() for i in lArrayImgLogic]), ddof=1, axis=0)
        lMeanLogic = np.mean(lVarMatLogic)

        lArrayImgBdba = MainRun.readRgba(bdbaFile, lwidth, lheight, 4)
        lVarMatBdba = np.var(np.vstack([i.ravel() for i in lArrayImgBdba]), ddof=1, axis=0)
        lMeanBdba = np.mean(lVarMatBdba)

        print("logic:%f,  bdba:%f"%(lMeanLogic, lMeanBdba))




if __name__ == "__main__":
    MainRun.runTest()
    # MainRun.testMat()
    # MainRun.testReadRgbaFile()
    # MainRun.calculateNoisy()
    MainRun.testDataCamera()