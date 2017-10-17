## Your name: Chalse Okorom
## The option you've chosen: 2

# Put import statements you expect to need here!
import tweepy
import twitter_info
import json
import sqlite3
import omdb
import itertools

#implement movie class definition
	#One instance of this class will represent a movie and it's attributes -- title, director, IMDB rating, actors, number of languages in movie, etc.

#implement tweets class definition

#implement users class definition

#implement a function called get_user_tweets(). it should gather at least 20 tweets using a search term parameter and return a list dictionaries of tweets.

#implement a function called request_movies(). it is detailed in the project plan.
	#This method will make a request to OMDB to obtain a list of dictionaries (in which each of the dictionaries contains all the information for one movie) based on the list of search terms given as input. Then, it will loop through the dictionaries to return a list of Movie instances.

#implement a function called get_neighborhood(). it is detailed in the project plan. You should use the infomration given from get_user_tweets()
	#This method will accept a list of tweets and find the users that have been mentioned in those tweets.

#create three databases: Tweets, Users, and Movies using the tweepy and omdb apis. Use the information gathered from the three above functions to load and commit the necessary data into the tables.
# Tweets:
# - tweet_id (containing the string id belonging to the Tweet itself, from the data you got from Twitter -- note the id_str attribute) -- this column should be the PRIMARY KEY of this table
# - text (containing the text of the Tweet)
# - user_id (an ID string, referencing the Users table, see below)
# - time_posted (the time at which the tweet was created)
# - retweets (containing the integer representing the number of times the tweet has been #retweeted)
# Users:
# - user_id (containing the string id belonging to the user, from twitter data -- note the id_str attribute) -- this column should be the PRIMARY KEY of this table
# - screen_name (containing the screen name of the user on Twitter)
# - num_favs (containing the number of tweets that user has favorited)
# - description (text containing the description of that user on Twitter)
# Movies:
# - movie title -- this column is the PRIMARY KEY
# - movie director
# - IMDB rating
# - number of languages in the movie

# MAKE TWO QUERIES TO THE DATABASE and save them in different variables.
# Select all tweets that a were posted from 10 am to 12pm.
# Join User screen names with Tweet user ids to see which of them match up.

# Write your test cases here.
class Tests(unittest.TestCase):
	def test_request_movies_one(self):
		#test that request_movies() returns a list.
	def test_request_movies_two(self):
		#test that request_movies() returns a list of movie objects.
	def test_movies_one(self):
		#test that my movies table has four columns
	def test_tweets(self):
		#test that the tweets table has five columns
	def test_neighborhood(self):
		#test that get_neighborhood() returns a list of user objects
	def test_select(self): 
		#test thatthe tweets selected were posted from 10am to 12pm
	def test_join(self):
		#test that the selected screen names and user ids are the same.
	def test_movie_dicts(self):
		#test that you can initialize a Movie instance with a dictionary.

## Remember to invoke all your tests...

if __name__ == "__main__":
	unittest.main(verbosity=2)