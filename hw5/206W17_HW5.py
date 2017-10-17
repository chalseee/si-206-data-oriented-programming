import unittest
import tweepy
import requests
import json
import twitter_info
import sys

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time: Friday/9AM
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and
	#prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in 
	#between each of them, e.g.

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

CACHE_FNAME = "hw5_cache.json"
try:
	cache_file = open(CACHE_FNAME, 'r')
	cache_contents = cache_file.read()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}

search_term = input('enter search term: ')

def get_three_tweets(string):
	if string in CACHE_DICTION:
		print('using cached data for', string)
		twitter_results = CACHE_DICTION[string]
	else:
		print('getting data from internet for', string)
		results = api.search(q=string)
		twitter_results = results['statuses']
		CACHE_DICTION[string] = twitter_results

		f = open(CACHE_FNAME, 'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()

	tweet_texts = []
	for t in twitter_results:
		tweet_texts.append(t)
	return tweet_texts[:3]

three_tweets = get_three_tweets(search_term)

for t in three_tweets:
	print("TEXT: " + t['text'])
	print("CREATED AT: " + t['created_at'])
	print ('\n')


print((len(three_tweets)))

