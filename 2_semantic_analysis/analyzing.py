#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
import pyLDAvis.gensim
from gensim.models import LdaModel
import pickle

corpus = pickle.load(open("../data/bow_docs", "rb"))
model = LdaModel.load("../data/lda_model")
vis = pyLDAvis.gensim.prepare(model, corpus, model.id2word)
pyLDAvis.show(vis)
