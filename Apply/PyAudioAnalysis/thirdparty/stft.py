import numpy as np
import matplotlib.pyplot as plt
import os
import wave
from PIL import Image

# 读入音频。
# 我音频的路径为E:\SpeechWarehouse\zmkm\zmkm0.wav
filename = 'audio1.wav'

# 打开语音文件。
f = wave.open(filename, 'rb')
# 得到语音参数
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# ---------------------------------------------------------------#
# 将字符串格式的数据转成int型
print("reading wav file......")
strData = f.readframes(nframes)
waveData = np.fromstring(strData, dtype=np.short)
# 归一化
waveData = waveData * 1.0 / max(abs(waveData))
# 将音频信号规整乘每行一路通道信号的格式，即该矩阵一行为一个通道的采样点，共nchannels行
waveData = np.reshape(waveData, [nframes, nchannels]).T  # .T 表示转置
f.close()  # 关闭文件
print("file is closed!")
# ----------------------------------------------------------------#
'''绘制语音波形'''
print("plotting signal wave...")
time = np.arange(0, nframes) * (1.0 / framerate)  # 计算时间
time = np.reshape(time, [nframes, 1]).T
plt.plot(time[0, :nframes], waveData[0, :nframes], c="b")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Original wave")
plt.show()

# --------------------------------------------------------------#
'''
    绘制频谱
        1.求出帧长、帧叠点数。且FFT点数等于每帧点数（即不补零）
        2.绘制语谱图
'''
print("plotting spectrogram...")
framelength = 0.025  # 帧长20~30ms
framesize = framelength * framerate  # 每帧点数 N = t*fs,通常情况下值为256或512,要与NFFT相等\
# 而NFFT最好取2的整数次方,即framesize最好取的整数次方

# 找到与当前framesize最接近的2的正整数次方
nfftdict = {}
lists = [32, 64, 128, 256, 512, 1024]
for i in lists:
	nfftdict[i] = abs(framesize - i)
sortlist = sorted(nfftdict.items(), key=lambda x: x[1])  # 按与当前framesize差值升序排列
framesize = int(sortlist[0][0])  # 取最接近当前framesize的那个2的正整数次方值为新的framesize

NFFT = framesize  # NFFT必须与时域的点数framsize相等，即不补零的FFT
overlapSize = 1.0 / 3 * framesize  # 重叠部分采样点数overlapSize约为每帧点数的1/3~1/2
overlapSize = int(round(overlapSize))  # 取整
print("帧长为{},帧叠为{},傅里叶变换点数为{}".format(framesize, overlapSize, NFFT))
spectrum, freqs, ts, fig = plt.specgram(waveData[0], NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize),
										noverlap=overlapSize, mode='default', scale_by_freq=True, sides='default',
										scale='dB', xextent=None)  # 绘制频谱图

plt.ylabel('Frequency')
plt.xlabel('Time')
plt.title("Spectrogram")
plt.show()


def getSpectrum(filename, window_length_ms, window_shift_times):

	# read data
	wav_file = wave.open(filename, 'r')
	params = wav_file.getparams()
	nchannels, sampwidth, framerate, wav_length = params[:4]
	str_data = wav_file.readframes(wav_length)
	wave_data = np.fromstring(str_data, dtype=np.short)
	wav_file.close()
	print(nchannels, sampwidth, framerate, wav_length)

	# gain log spectrogram
	window_length = int(framerate * window_length_ms / 1000)  # change time to points number
	Win_hamming = np.hamming(window_length)
	window_shift = int(window_length * window_shift_times)  # change time to points number
	nframe = (wav_length - (window_length - window_shift)) / window_shift  # gain frame number
	spec = np.zeros((int(window_length / 2), int(nframe)))  # store spectrogram [only half part]
	for i in range(int(nframe)):
		start = i * window_shift
		end = start + window_length
		spec[:, i] = np.log1p(np.abs(np.fft.fft(Win_hamming * wave_data[start:end])))[:int(window_length / 2)]

	return spec

# main process
speech_spectrum = getSpectrum(filename, 20, 0.5)
plt.imshow(speech_spectrum[:, :])
speech_spectrum = speech_spectrum[::-1, :]
speech_spectrum = speech_spectrum / np.max(speech_spectrum)
im = Image.fromarray(np.uint8(speech_spectrum * 255))
im = im.resize((256, 256))
im.save('spec1.jpg')
#plt.xlim(0, 20)
#plt.ylim(0, 80)
plt.show()