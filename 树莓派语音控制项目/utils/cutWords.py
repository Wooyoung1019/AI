import jieba
from 案例2 import words


def init_KeyWord():
    for i in words.KEY_WORDS: # 遍历关键字
        jieba.add_word(i) # 在程序中动态修改词典

def cut_VocieTxt(audioTxt):
    if audioTxt['err_no'] ==3307:
        return ['无']
    if len(audioTxt['result']) > 0:
        # 对语音识别返回的文本进行分词
        result = list(jieba.cut(audioTxt['result'][0]))
        print(result)
    else:
        result = ['无']
    return result
