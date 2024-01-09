import audioop

from aip import AipSpeech
import pyaudio
import wave, time
import numpy as np
from pyaudio import PyAudio, paInt16
from utils.cutWords import init_KeyWord, cut_VocieTxt

# 用户语音输入01
def save_voice(path):
    pa = PyAudio()
    wf = wave.open(path, 'wb') # 打开wave文件
    wf.setnchannels(1) # 配置声道数
    wf.setsampwidth(2) # 采样宽度2bytes
    wf.setframerate(16000) # 采样率
    stream = pa.open(format=paInt16, channels=wf.getnchannels(),
                     rate=wf.getframerate(), input=True,
                     frames_per_buffer=1024) # 打开i一个stream
    buff = [] # 存储声音信息
    start = time.time() # 开始运行时间戳
    print('用户输入：', end='')
    while time.time() < start+5: # 录制5秒
        buff.append(stream.read(wf.getframerate()))
    stream.close() # 关闭stream
    pa.terminate()
    wf.writeframes(b''.join(buff))
    wf.close() # 关闭wave

# 读取文件，参数为wav文件路劲
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别音频文件的txt文件，参数为百度AI创建应用的密钥信息
def get_vocie_txt(AppID, API_Key, Secret_Key):
    client = AipSpeech(AppID, API_Key, Secret_Key) # 设置百度API的密钥信息
    vodie_txt = client.asr(get_file_content('./audio/temp.wav'), 'wav', 16000,{
        'dev_pid':1537,
    })
    return vodie_txt

# 监控并录音
def Monitor():
    CHUNK = 1024 # 区块大小
    FORMAT = pyaudio.paInt16 # 格式
    CHANNELS = 1 # 单声道
    RATE = 16000 # 采样率
    WAVE_OUTPUT_FILENAME = './audio/temp.wav' # 文件位置和文件名
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('开始缓存录音')
    low_audio_flag = 0
    detect_count = 0
    out_flag = 0
    frames = []
    while True:
        detect_count += 1
        stream_data = stream.read(CHUNK)
        rms = audioop.rms(stream_data, 2)
        if rms > 1000:
            out_flag = 1
            low_audio_flag = 0
        else:
            low_audio_flag += 1
        if low_audio_flag > 30 and out_flag == 1:
            print('**没有听到声音**')
            break
        if out_flag == 1:
            frames.append(stream_data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# 循环监听麦克风
AppID = '34426540'
API_Key = '5HeZfSqX5D5H5lu0tbj7pBfc'
Secret_Key = 'Vaz4LZU3jPzcmLgKbYHjb8frxEY7o62x'

if __name__ == '__main__':
    while(True):
        Monitor()
        print('循环监听')
        audioTxt = get_vocie_txt(AppID, API_Key, Secret_Key)
        print(audioTxt)
        cut_VocieTxt(audioTxt)
        time.sleep(5)