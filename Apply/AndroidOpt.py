# -*- coding: utf-8 -*-

import sys, os, time
import subprocess


def tapScreen(x, y):
    """calculate real x, y according to device resolution."""
    # base_x, base_y = 1920, 1080
    # real_x = int(x / base_x * device_x)
    # real_y = int(y / base_y * device_y)
    subprocess.call( 'D:\\Program Files\\Nox\\bin\\adb.exe shell  input tap %d %d '%(x,y))


def clickScreen():
    lExe = "D:\\Program Files\\Nox\\bin\\adb.exe"
    lCmd = str.format('%s shell  input tap %d %d '%(lExe, 300,400 ))
    subprocess.call(lCmd)


def screenShoot():
    lExe = "D:\\Program Files\\Nox\\bin\\adb.exe"
    lShoot = str.format("%s  pull /sdcard/screenshot.png %s "%(lExe, os.getcwd()))
    lCmd1 = str.format("%s shell /system/bin/screencap -p /sdcard/screenshot.png "%(lExe))
    subprocess.call(lCmd1)
    subprocess.call(lShoot)


class MainTest():
    @staticmethod
    def testScreenShoot():
        screenShoot()

    @staticmethod
    def testClick():
        tapScreen(733,451)



if __name__ == "__main__":
    print os.getcwd()
    # MainTest.testScreenShoot()
    MainTest.testClick()