#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
import wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pathlib import Path


def get_stop_words() -> set:
    res = set()
    for file in Path("../data/stopwords").iterdir():
        if file.suffix == ".txt":
            res |= set(file.read_text(encoding="utf-8").splitlines())
    return res


with open("../data/words.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()
# mask = None
mask = np.array(Image.open("../data/image.jpg"))
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
plt.savefig("../output/wordcloud.png")
plt.show()
