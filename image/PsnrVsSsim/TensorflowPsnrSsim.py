# -*- coding: utf-8 -*-

import sys, os, time
import tensorflow as tf

class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img1 = os.path.join(_tarDir, u"ShareMedia/Images/woman0.jpg")
    _img2 = os.path.join(_tarDir, u"ShareMedia/Images/woman0_2.jpg")

    @classmethod
    def runTest(cls):
        print(u"hello world")

    @classmethod
    def testTensorFlow(cls):
    # Read images from file.
     im1 = tf.image.decode_jpeg(cls._img1)
     im2 = tf.image.decode_jpeg(cls._img2)
     # Compute PSNR over tf.uint8 Tensors.
     psnr1 = tf.image.psnr(im1, im2, max_val=255)
     print( tf.Session.run(psnr1) )

     # Compute PSNR over tf.float32 Tensors.
     # im1 = tf.image.convert_image_dtype(im1, tf.float32)
     # im2 = tf.image.convert_image_dtype(im2, tf.float32)
     # psnr2 = tf.image.psnr(im1, im2, max_val=1.0)
     # psnr1 and psnr2 both have type tf.float32 and are almost equal.




if __name__ == "__main__":
    MainRun.runTest()
    MainRun.testTensorFlow()
