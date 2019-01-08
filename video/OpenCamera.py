# -*- coding: utf-8 -*-

import os

import PIL.Image
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


def DisplayCameraInOne():
    cap = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    if cap.isOpened():
        # get vcap property
        width = int (cap.get(cv2.CAP_PROP_FRAME_WIDTH  ) ) # float
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))  # float


    while (1):
        # get a frame
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()
        imgList = []
        imgList.append(convertCvToPil(frame))
        imgList.append(convertCvToPil(frame2))
        from image import ImageCompose
        tarImg = ImageCompose.imageJiontByRaw(imgList, width, height, ImageCompose.OptImg.horizontal)

        # show a frame
        cv2.imshow("capture", tarImg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cap2.release()
    cv2.destroyAllWindows()



def convertCvToPil(tImg):
    cv2_im = cv2.cvtColor(tImg,cv2.COLOR_BGR2RGB)
    pil_im = PIL.Image.fromarray(cv2_im)
    return pil_im


class MainTest():
    @staticmethod
    def testOpenCamera():
        OpenCamera()

    @staticmethod
    def testOpenMultiCamera():
        OpenMultiCameras()

    @staticmethod
    def testMutilScreen():
        DisplayCameraInOne()


if __name__ == "__main__":
    print os.getcwd()
    MainTest.testMutilScreen()