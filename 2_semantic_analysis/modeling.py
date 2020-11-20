#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
from gensim.models import LdaModel
from pathlib import Path
import pandas as pd
import jieba
from zhon.hanzi import punctuation
import re
import pickle


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


from gensim import corpora

stopwords = get_stop_words()
docs = []
for file in Path("../data").iterdir():
    if not file.suffix == ".csv":
        continue
    df = pd.read_csv(file)
    for comment in df.comments:
        processed = re.sub(f"[{punctuation}]", "", comment)
        processed = format_str(processed)
        words = [word for word in jieba.cut(processed) if word not in stopwords]
        if len(words) > 3:
            docs.append(words)
dictionary = corpora.Dictionary(docs)
bow_docs = [dictionary.doc2bow(doc) for doc in docs]
lda_model = LdaModel(
    corpus=bow_docs, id2word=dictionary, alpha="auto", eta="auto",
    iterations=400, num_topics=5,  # 建立多少个话题
    passes=20, eval_every=None
)
trans = lda_model[bow_docs]
pickle.dump(bow_docs, open("../data/bow_docs", "wb"))
lda_model.save("../data/lda_model")
dictionary.save("../data/dictionary")
