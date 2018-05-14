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
    # print p.get_default_output_device_info()

    lpcm = open(u"temp.pcm","wb")
    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
          data = wf.readframes(frame_count)
          if lpcm is not None:
              lpcm.write(data)
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
    lpcm.close()
    # close PyAudio (7)
    p.terminate()



class MainTest():
    @staticmethod
    def TestAudioPlay():
        lFile = u"TestAudio.WAV"
        playWave(lFile)
        pass

    @staticmethod
    def TestAudioPlayCallbk():
        lFile = u"TestAudio.WAV"
        playWavebyCallback(lFile)
        pass




if __name__ == "__main__":
    print os.getcwd()
    # MainTest.TestAudioPlay()
    MainTest.TestAudioPlayCallbk()