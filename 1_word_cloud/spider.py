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
import sys

# 26100958  复联4
# 26794435  哪吒
# 25765735  金刚狼
# 1851857   蝙蝠侠
# 26374197  蜘蛛侠

headers = {
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Content-Type": "text/application"
}
results = []
cur_path = Path(__file__).parent

if len(sys.argv) > 1:
    id2name = {}
    for i in range(1, len(sys.argv), 2):
        id2name[sys.argv[i]] = sys.argv[i + 1]
else:
    id2name = {
        "26100958": "复联4"  # 默认爬取复联4
    }
for movie_id, movie_name in id2name.items():
    for i in range(10):
        # 根据你想爬取电影的url
        url = f"https://movie.douban.com/subject/{movie_id}/comments"
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
    Path(f"{cur_path}/../data").mkdir(parents=True, exist_ok=True)
    df.to_csv(f"{cur_path}/../data/comments_{movie_name}.csv", index=False)
