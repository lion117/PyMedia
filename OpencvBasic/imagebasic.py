# -*- coding: utf-8 -*-

import sys, os, time
import  cv2



class MainRun():
    lImgDir = os.path.join(os.path.dirname(os.getcwd()), u"ShareMedia/Images")
    _img1 = os.path.join(lImgDir,u"cat0.jpg")


    @classmethod
    def testRead(cls):
        if os.path.exists(cls._img1) is False:
            print("file is not exist %s"%(cls._img1))
            return
        lObjImg = cv2.imread(cls._img1,cv2.IMREAD_ANYCOLOR)
        cv2.imshow("show image",lObjImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @classmethod
    def testWriteImg(cls):
        if os.path.exists(cls._img1) is False:
            print("file is not exist %s" % (cls._img1))
            return
        lObjImg = cv2.imread(cls._img1, cv2.IMREAD_ANYCOLOR)
        lObjGray = cv2.cvtColor(lObjImg, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(u"gray_cat0.png",lObjGray)
        cv2.imshow("show image",lObjGray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()








if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.testRead()
    MainRun.testWriteImg()