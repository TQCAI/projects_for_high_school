#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
# -*- coding: utf-8 -*-
# __author__ = 'Carina'
import requests
import pandas as pd
from lxml import etree
from pathlib import Path

headers = {
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Content-Type": "text/application"
}
results = []
for i in range(10):
    # 根据你想爬取电影的url
    url = "https://movie.douban.com/subject/26100958/comments"
    url += f"?start={i * 20}&limit=20&status=P&sort=new_score"

    r = requests.get(url, headers=headers).content.decode('utf-8')
    s = etree.HTML(r)
    for i in range(1, 21):
        comments = s.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span')
        if len(comments) > 0:
            comment = comments[0].text
            results.append(comment)
            print(comment)
df = pd.DataFrame(pd.Series(results), columns=["comments"])
Path("../data").mkdir(parents=True, exist_ok=True)
df.to_csv("../data/comments.csv", index=False)
