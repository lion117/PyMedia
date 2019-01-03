# -*- coding: utf-8 -*-

import sys, os, time
import  cv2


class MainRun():

    @staticmethod
    def runVideo():
        lVHandle = cv2.VideoCapture(0)
        if lVHandle.isOpened():
            lVHandle.set(cv2.CAP_PROP_FRAME_HEIGHT  ,1080)
            lVHandle.set(cv2.CAP_PROP_FRAME_WIDTH ,1920)
        while True:
            lRet, lFrame = lVHandle.read()
            if lRet is False:
                break
            cv2.imshow('720p', lFrame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.release()
        cv2.destroyAllWindows()



    @staticmethod
    def run1080pVideoPhone():
        cap2 = cv2.VideoCapture(0)
        cap = cv2.VideoCapture(1)
        if cap.isOpened():
            lHeight = 1080
            lWidth  = 1920
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT  ,lHeight)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH ,lWidth)
            # cap.set(cv2.CAP_PROP_FRAME_HEIGHT  ,720)
            # cap.set(cv2.CAP_PROP_FRAME_WIDTH ,960)
        # if cap2.isOpened():
        #     cap2.set(cv2.CAP_PROP_FRAME_HEIGHT  ,720)
        #     cap2.set(cv2.CAP_PROP_FRAME_WIDTH ,960)

        lIndex  = 0
        while (1):
            # get a frame
            ret, frame = cap.read()
            ret2, frame2 = cap2.read()
            # show a frame
            frame = MainRun.CutImg(frame)
            # frame2 = MainRun.CutImg(frame2)
            cv2.imshow("1080p", frame)
            # cv2.imshow("720p", frame2)
            # lFileName = str.format("Img_%dx%d_%d.jpg"%( lWidth, lHeight,lIndex))
            # lIndex+=1
            # cv2.imwrite(lFileName,frame)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        cap.release()
        # cap2.release()
        cv2.destroyAllWindows()

    @staticmethod
    def runSaveVideoForPhone():
        cap = cv2.VideoCapture(2)
        # cap2 = cv2.VideoCapture(1)
        if cap.isOpened():
            lHeight = 720
            lWidth = 960
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, lHeight)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, lWidth)
            # cap.set(cv2.CV_CAP_PROP_FOURCC, cv2.CAP_OPENCV_MJPEG)

            # cap.set(cv2.CAP_PROP_FRAME_HEIGHT  ,720)
            # cap.set(cv2.CAP_PROP_FRAME_WIDTH ,960)
        # if cap2.isOpened():
        #     cap2.set(cv2.CAP_PROP_FRAME_HEIGHT  ,720)
        #     cap2.set(cv2.CAP_PROP_FRAME_WIDTH ,960)

        lFileName = str.format("video_%dx%d_%d.wmv"%(lWidth, lHeight,time.time()))
        lCodec = cv2.VideoWriter_fourcc(*'WMV2')
        lWriter = cv2.VideoWriter(lFileName, lCodec, 30, (lHeight * 9 / 16, lHeight))

        while (1):
            # get a frame
            ret, frame = cap.read()
            # ret2, frame2 = cap2.read()
            # show a frame
            frame = MainRun.CutImg(frame)
            # frame2 = MainRun.CutImg(frame2)
            cv2.imshow("1080p", frame)
            # cv2.imshow("720p", frame2)
            lWriter.write(frame)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        cap.release()
        lWriter.release()
        # cap2.release()
        cv2.destroyAllWindows()





    @classmethod
    def CutImg(cls, tImgSrc):
        lSrcHeight,lSrcWidth,lBit = tImgSrc.shape
        lDestWidth = lSrcHeight*9/16
        lDestHeight = lSrcHeight
        lTopX, lTopY = ( (lSrcWidth - lDestWidth)/2 ,0)
        lButtonX, lButtonY = ( lSrcWidth/2 + lDestWidth/2 , lSrcHeight)
        lDestImg = tImgSrc[lTopY: lButtonY , lTopX : lButtonX]
        # if lDestHeight == 720:
        #     lDestImg = cv2.resize(lDestImg, (1080*9/16, 1080))

        lText = str.format("img src height %d"%(lSrcHeight))
        lDestImg = cv2.putText(lDestImg,lText ,(50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
        return  lDestImg





if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.runVideo()
    # MainRun.run1080pVideoPhone()
    # MainRun.run1080pVideoPhone()
    MainRun.runSaveVideoForPhone()