# -*- coding: utf-8 -*-

import sys, os, time

import pyaudio
import numpy as np
import pylab
import time

RATE = 44100
CHUNK = int(RATE/20) # RATE/number of updates per second


def visualizeMusic():

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    for i in range(int(20 * RATE / CHUNK)):
        # for 10 seconds
        t1 = time.time()  # time starting
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        pylab.plot(data)
        pylab.title("test")
        pylab.grid()
        pylab.axis([0, len(data), -2 ** 8, 2 ** 8])
        pylab.savefig("sound.png", dpi=50)
        pylab.show(block=False)
        time.sleep(0.5)
        print("took %.2f ms." % (time.time() - t1) * 1000)
    pylab.close('all')
    stream.stop_stream()
    stream.close()
    p.terminate()


def sound_plot(stream):
    t1 = time.time()  # time starting
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    pylab.plot(data)
    pylab.title("test")
    pylab.grid()
    pylab.axis([0, len(data), -2 ** 8, 2 ** 8])
    pylab.savefig("sound.png", dpi=50)
    pylab.show(block=False)
    time.sleep(0.5)
    pylab.close('all')
    print("took %.2f ms." % (time.time() - t1) * 1000)




if __name__ == "__main__":
    visualizeMusic()
    print os.getcwd()