import wave
import numpy as np
from scipy import signal
 
wf = wave.open("data/output/output.wav", "rb")
nchannels = wf.getnchannels()
sampwidth = wf.getsampwidth()
framerate = wf.getframerate()
nframes = wf.getnframes()
 
duration = nframes / framerate
print("音频文件时长：%.2fs" % duration)
 
# 设置分割的长度为2s
length = 2 * framerate
start = 0
 
for i in range(5):
    # 截取片段
    wf.setpos(start)
    data = wf.readframes(length)
 
    # 保存为新文件
    new_wf = wave.open("data/audio_slicing/segment_%d.wav" % i, "wb")
    new_wf.setnchannels(nchannels)
    new_wf.setsampwidth(sampwidth)
    new_wf.setframerate(framerate)
    new_wf.writeframes(data)
    new_wf.close()
    
    # 更新起始位置
    start += length