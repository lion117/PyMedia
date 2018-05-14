# -*- coding: utf-8 -*-

import sys, os, time


"""PyAudio Example: Play a wave file."""


import pyaudio
import wave
import time
import sys

CHUNK = 1024



def playWave(tFile):
    wf = wave.open(tFile, 'rb')
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()


def playWavebyCallback(tFile):
    """PyAudio Example: Play a wave file (callback version)."""

    wf = wave.open(tFile, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()

import pyaudio
import numpy as np
import pylab
import time

def visualizeMusic():
    RATE = 44100
    CHUNK = int(RATE/20) # RATE/number of updates per second

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    for i in range(int(20 * RATE / CHUNK)):
        # for 10 seconds
        sound_plot(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()


def sound_plot(stream):
    t1 = time.time()  # time starting
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    pylab.axis([0, len(data), -2 ** 8, 2 ** 8])
    pylab.savefig("sound.png", dpi=50)
    pylab.show(block=False)
    time.sleep(0.5)
    pylab.close('all')
    print("took %.2f ms." % (time.time() - t1) * 1000)





if __name__ == "__main__":
    print os.getcwd()