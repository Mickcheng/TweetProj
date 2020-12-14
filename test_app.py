import unittest
import os
import requests



class FlaskTests(unittest.TestCase):
	
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.tweet = {
		
			'tweet_test': 'If Sheena Monnin apologized for her mistake, as she should have, I would have treated her very nicely',
			'tweet_resp': ["Ted Cruz complains about my views on eminent domain, but without it we wouldn't have roads, highways, airports, schools or even pipelines.",
							 '"@JimmyGould07: Only one man has the appeal, nerve, commitment, ideas, & motivation. He\'s the icon, business tycoon, and lovable DonaldTrump',
							 'President Obama, if it is important to you, I will substantially increase the $5M offer!',
							 'President Obama, if it is important to you, I will substantially increase the $5M offer!',
							 "Mark my words, a gallon of gas will be $5 during the summer. OPEC is ripping us off. There's nobody in our (cont) http://tl.gd/fvm4kv\xa0",
							 'In the last 2 weeks, I had $35M of negative ads against me in Florida & I won in a massive landslide.The establishment should save their $$!',
							 'I went to Wharton, made over $8 billion, employ thousands of people & get insulted by morons who can’t get enough of me on twitter...!',
							 'Vision remains vision until you focus, do the work, and bring it down to earth where it will do some good.',
							 'Have you ever seen our country look weaker or more pathetic: Snowden, ObamaCare, VA, Russia, jobs, decimated military, debt and so much more',
							 "I hear the Rickets family, who own the Chicago Cubs, are secretly spending $'s against me. They better be careful, they have a lot to hide!",
							 'I was invited to be with Mitt Romney tonight --- win, lose, or draw, I’ll be there!',
							 'Wow, I’m at 2,200,000  followers but I’d love to get rid of the haters & losers—they’re such a waste of time!',
							 'I have been leading big in all  polls, with two more today, @nbc and @CNN. The NBC poll is more than double next,  at 29%. Fiorina has 11%.',
							 'With the run on our dollar about to take place, commodity prices will rise. Gold, silver, & timber will spike-- also, certain real estate.',
							 "With our record debt & trillion $ deficits, our $ is now at an all-time low against the Chinese Yuan. Time for our gov't to work together.",
							 'Terrible CBO forecast for 2013--1.4% GDP growth and 7.5%+ unemployment (really 17%+) http://bit.ly/XVEZSr\xa0  You get what you vote for!',
							 "If you are steadfast in your efforts, critics will be harmless. Achievers move forward, and achievement is not a plateau, it's a beginning.",
							 'Wow, the MSM is really going after me. 12,000 in Sarasota, a love fest, hardly a mention. Only one negativity - they only want negatives!',
							 'I watched @todayshow this AM re: @MarthaStewart & dating. She looks terrific, better than ever, any guy would be lucky to be with her.',
							 'I was invited to be with Mitt Romney tonight --- win, lose, or draw, I’ll be there!']
		}
		pass

	def tearDown(self):
		pass
		
	def test_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)		
		
	"""def test_get_tweets(self):
		params = {
					'twt_test' : self.tweet['tweet_test']
					
		}
		self.assertEqual(len(app.get_tweets(tweet_test)), 20)"""
	
	def test_sent(self):
		params = {'tweet_resp': 'positive'}
		responce = requests.get('http://localhost:5000',data=params)
		self.assertEqual(responce.status_code, 200)
		
	
if __name__ == '__main__':
	unittest.main()	
