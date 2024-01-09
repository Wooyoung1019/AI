from aip import AipSpeech

# 读取文件，参数为wav文件路劲
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别音频文件的txt文本，参数为百度ai创建应用的密钥信息
def get_vocie_txt(APP_ID, API_KEY, SECRET_KEY):
    #设置百度api的密钥信息
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    #调用百度语音识别，参数为音频文件流，文件格式，码率，识别pid
    vocie_txt = client.asr(get_file_content("./audio/16k.wav"), 'wav', 16000, {'dev_pid': 1537,})
    return vocie_txt