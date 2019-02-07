# -*- coding: utf-8 -*-
"""
@author: Leo
Date:  2019/2/2
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os
import  matplotlib.pyplot as plt
import  numpy




class MainRun():
    lTarDir = os.path.dirname(os.path.dirname(os.getcwd()))
    lImg0 = os.path.join(lTarDir,u"ShareMedia/Images/cat0.jpg")

    @classmethod
    def runDemo(cls):
        print("hello world")


    @classmethod
    def runBaic2d(cls):
        plt.figure()
        x = numpy.linspace(-1,1,100)
        y = x**2
        plt.xlim((-0.5,0.5))
        plt.ylim((0,0.5))
        plt.xlabel(u"x ax")
        plt.ylabel(u"y ax")

        plt.plot( x ,y ,color ='green', linewidth ='1',linestyle='-')
        plt.show()

    @classmethod

    def runBomb(cls):
        plt.figure()
        x = numpy.linspace(-2, 2, 50)
        y = x**2
        plt.plot(x,y, color = "red")
        x1 = numpy.linspace(2,6,50)
        y1 = (x1-4)**2
        plt.plot(x1,y1,color = "red")
        ax1 = plt.gca()
        ax1.spines["right"].set_color("none")
        ax1.spines["top"].set_color("none")
        ax1.xaxis.set_ticks_position("bottom")
        ax1.yaxis.set_ticks_position("left")
        ax1.spines["left"].set_position(("data",2))
        ax1.spines["bottom"].set_position(("data",1))

        plt.scatter([0,],[0,],color="blue",s=50)
        plt.scatter([4,],[0,],color="blue",s=50)
        plt.text(-0.5, 4, r'$y=x^2$',
                 fontdict={'size': 16, 'color': 'r'})

        x2  =0
        x3 =4
        plt.plot([0,0,],[0,1,],color="b",linestyle="--")
        plt.plot([4,4,],[0,1,],color="b",linestyle="--")
        # plt.xlim((-0.5, 0.5))
        # plt.ylim((0, 0.5))

        plt.show()


    @classmethod
    def runDistGrayImag(cls):







if __name__ == '__main__':
    # MainRun.runDemo()
    # MainRun.runBaic2d()
    MainRun.runBomb()
