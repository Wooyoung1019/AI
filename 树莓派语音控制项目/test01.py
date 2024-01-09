import re
import random
import requests
import time

import requests

# 获取网页HTML代码

# pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
# resp = requests.get('https://www.sohu.com/')
# if resp.status_code == 200:
#     all_matches = pattern.findall(resp.text)
#     print(resp.text)
#     for href, title in all_matches:
#         print('href:'+href)
#         print('title:'+title)


for page in range(1, 11):
    resp = requests.get(url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})

    pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
    titles = pattern1.findall(resp.text)
    # 通过正则表达式获取class属性为rating_num的span标签并用捕获组提取标签内容
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    ranks = pattern2.findall(resp.text)
    # 使用zip压缩两个列表，循环遍历所有的电影标题和评分
    for title, rank in zip(titles, ranks):
        print(title, rank)
        # 随机休眠1-5秒，避免爬取页面过于频繁
    time.sleep(random.random() * 4 + 1)