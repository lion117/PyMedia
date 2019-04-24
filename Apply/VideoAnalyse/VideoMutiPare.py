# -*- coding: utf-8 -*-

import sys, os, time
import  cv2

class MainRun():

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def compareCamera(cls):
        cap = cv2.VideoCapture(6)   #   YY
        cap2 = cv2.VideoCapture(0)  #  SRC
        while (1):
            # get a frame
            ret, frameYY = cap.read()
            ret2, frameSRC = cap2.read()
            # show a frame
            cv2.imshow("YY", MainRun.analyseImg(frameYY))
            cv2.imshow("SRC", MainRun.analyseImg(frameSRC))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # cap.release()
        cap2.release()
        cv2.destroyAllWindows()

    @classmethod
    def analyseImg(cls,tFrame):
        lB,lG,lR = cv2.split(tFrame)
        HSV = cv2.cvtColor(tFrame, cv2.COLOR_BGR2HSV)
        lH, lS, lV = cv2.split(HSV)
        lTxt = str.format("R: %d G: %d, B: %d  H: %d S: %d V: %d"%(cv2.mean(lR)[0],cv2.mean(lG)[0],cv2.mean(lB)[0],cv2.mean(lH)[0],cv2.mean(lS)[0],cv2.mean(lV)[0]))
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(tFrame,lTxt,(80,100),font,1,(0,255,0),1,cv2.LINE_AA)
        return tFrame




if __name__ == "__main__":
    MainRun.runTest()
    MainRun.compareCamera()