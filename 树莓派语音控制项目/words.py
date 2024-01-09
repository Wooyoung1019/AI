import jieba
import words

KEY_WORDS = [
    "名字是什么",
    "名字叫什么",
    "你叫什么名字",
    "小明同学",
    "打开台灯",
    "关闭台灯",
    "天气",
    "明天"
]

def init_KeyWord():
    for i in words.KEY_WORDS: # 便利关键字
        jieba.add_word(i) # 在程序中动态修改词典

def cut_VocieTxt(audioTxt):
    if audioTxt['err_no'] == 3307:
        return ['无']
    if len(audioTxt['result']) > 0:
        # 对语音识别返回的文本进行分词
        result = list(jieba.cut(audioTxt['result'][0]))
        print(result)
    else:
        result = ['无']
    return result