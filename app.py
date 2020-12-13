from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import os
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

from nltk.tokenize import TweetTokenizer
from flask import Markup

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
	return render_template("index.html")

@app.route('/result', methods=['POST'])	
def sent():
	if request.method == 'POST':
		result = request.form
		text = result['sentences']
		sent = get_tweets(text)
		
			
	return render_template("result.html", result = sent)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
