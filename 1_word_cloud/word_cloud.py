#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
import re
import pandas as pd
from zhon.hanzi import punctuation
import jieba
import sys
import wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pathlib import Path


# 26100958  复联4
# 26794435  哪吒
# 25765735  金刚狼
# 1851857   蝙蝠侠
# 26374197  蜘蛛侠

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def format_str(content):
    res = ""
    for c in content:
        if ord(u'\u4e00') <= ord(c) <= ord(u'\u9fa5'):
            res += c
    return res


def get_stop_words() -> set:
    res = set()
    for file in Path("../data/stopwords").iterdir():
        if file.suffix == ".txt":
            res |= set(file.read_text(encoding="utf-8").splitlines())
    return res


movie_name = "复联4"
if len(sys.argv) > 1:
    movie_name = sys.argv[1]
df = pd.read_csv(f"../data/comments_{movie_name}.csv")
txt = ""
for comment in df.comments:
    processed = re.sub(f"[{punctuation}]", "", comment)
    processed = format_str(processed)
    txt += processed

words = jieba.cut(txt)
res = []
for word in words:
    if len(word) > 1:
        res.append(word)
with open("../data/words.txt", "w+", encoding="utf-8") as f:
    f.write("\n".join(res))

with open("../data/words.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()
# mask = None
mask = np.array(Image.open(f"../data/{movie_name}.jpg"))
stopwords = get_stop_words()
wc = wordcloud.WordCloud(
    font_path="simkai.ttf",  # 指定字体类型
    background_color="white",  # 指定背景颜色
    max_words=200,  # 词云显示的最大词数
    max_font_size=255,  # 指定最大字号
    mask=mask,  # 指定模板
    scale=4,
    stopwords=stopwords
)
wc = wc.generate(" ".join(words))  ## 生成词云
Path("../output").mkdir(parents=True, exist_ok=True)
plt.figure(figsize=(8, 8), dpi=200)
plt.imshow(wc)
plt.axis("off")
plt.savefig(f"../output/wordcloud_{movie_name}.png")
plt.show()
