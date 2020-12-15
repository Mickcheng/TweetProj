#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import numpy as np
from joblib import dump
import gensim 
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from gensim.models.doc2vec import TaggedDocument,Doc2Vec
from nltk.tokenize import TweetTokenizer
nltk.download('punkt')
nltk.download('stopwords')





MODEL_DIR = os.environ["MODEL_DIR"]

MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR,MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

print("loading dataset...")
df = pd.read_csv('tweets.csv')
ab = df.copy()
ab = ab['text']

tknzr = TweetTokenizer()
df['text'] = df['text'].apply(lambda x: tknzr.tokenize(x.lower()))

stopWords = stopwords.words('english')
df['text'] = df['text'].apply(lambda x: [item for item in x if item not in stopWords])

a = df['text']


tagged_data = [TaggedDocument(words=a, tags=[str(i)]) for i, a in enumerate(ab)]

max_epochs = 20
vec_size = 20


model = Doc2Vec(vector_size=vec_size,min_count=1,dm=1)

model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=max_epochs)



print("serializing metadata to {}".format(METADATA_PATH))
dump(model, MODEL_PATH)


