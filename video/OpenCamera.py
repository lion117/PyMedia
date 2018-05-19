# -*- coding: utf-8 -*-

import sys, os, time


import cv2


def OpenCamera():
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



def OpenMultiCameras():
    cap = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    while(1):
        # get a frame
        ret, frame = cap.read()
        ret2,frame2 = cap2.read()
        # show a frame
        cv2.imshow("capture", frame)
        cv2.imshow("cap2",frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cap2.release()
    cv2.destroyAllWindows()



class MainTest():
    @staticmethod
    def testOpenCamera():
        OpenCamera()

    @staticmethod
    def testOpenMultiCamera():
        OpenMultiCameras()


if __name__ == "__main__":
    print os.getcwd()
    MainTest.testOpenMultiCamera()