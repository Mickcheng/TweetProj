#!/usr/bin/env python
# coding: utf-8
from flask import Flask, request, render_template

import os
import time
from joblib import load
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd
import joblib
import gensim 
from nltk.tokenize import TweetTokenizer
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
from prometheus_client import Histogram
import random
import time

REQUESTS = Counter('flask_app_calls_total','How many time the app was called')
EXCEPTIONS = Counter('flask_app_exceptions_total','How many time the app was trigger')
INPROGRESS = Gauge('flask_app_inprogress', 'number of requests in progress' )
LAST = Gauge('Flask_app_last_time_seconds','the last time of our app was called')
LATENCY_SUM = Summary('Flask_app_latency_summary_seconds','time needed for a progress')
LATENCY_HIS = Histogram('Flask_app_latency_histogram_seconds','time needed for a progress', buckets=[0.00001, 0.0001, 0.001,0.01,1.0,2.0,3.0,4.0])

app = Flask(__name__)
MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)
# Load model
print("Loading model from: {}".format(MODEL_PATH))
model = load(MODEL_PATH)
	# #############################################################################
df = pd.read_csv('tweets.csv')
ab = df.copy()
ab = ab['text']
def get_tweets(sentences):
	
	tknzr = TweetTokenizer()
	text = tknzr.tokenize(sentences.lower())
	stopWords = stopwords.words('english')
	text = [w for w in text if not w in stopWords] 
	
	
	mod = model.infer_vector(text)
	similar_doc = model.docvecs.most_similar([mod], topn=20)
	y = 0
	z = 1
	result= []
	for i in range(20):
    
		#print("{}".format(z),ab[int(similar_doc[y][0])],"\n")
		result.append(ab[int(similar_doc[y][0])]+'\n')
		
    
		y=y+1
		z=z+1
	
	return (result)
	

	
@app.route('/')
def index():
	LAST.set(time.time())
	REQUESTS.inc()
	start = time.time()
	with EXCEPTIONS.count_exceptions():
		if random.random() <0.2:
			raise Exception
	INPROGRESS.inc()
	time.sleep(5)
	lat = time.time()
	LATENCY_SUM.observe(lat -start)
	LATENCY_HIS.observe(lat -start)
	return render_template("index.html")

@app.route('/result', methods=['POST'])	
def sent():
	INPROGRESS.inc()
	time.sleep(2)
	if request.method == 'POST':
		
		result = request.form
		text = result['sentences']
		sent = get_tweets(text)
		
	INPROGRESS.dec()		
	return render_template("result.html", result = sent)

if __name__ == '__main__':
	start_http_server(8010)
	app.run(host='0.0.0.0')
