import unittest
import os
import requests
import app.py


class FlaskTests(unittest.TestCase):
	
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.tweet = {
			'tweet_test': 'If Sheena Monnin apologized for her mistake, as she should have, I would have treated her very nicely',
		}
		pass

	def tearDown(self):
		pass
		
	def test_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)		
		
	def test_get_tweets(self):
		params = {
					'twt_test' : self.tweet['tweet_test']
					
		}
		self.assertEqual(len(app.get_tweets(tweet_test)), 20)
	
	def test_sent(self):
		params = {'tweet_resp': 'positive'}
		responce = requests.get('http://localhost:5000',data=params)
		self.assertEqual(responce.status_code, 200)
		
	
if __name__ == '__main__':
	unittest.main()	

	
