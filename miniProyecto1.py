# -*- coding: utf-8 -*-
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1027638254-xcjZ79DXjbigRk9jJQw32g8v1fdMF17mpP9LTaF'
ACCESS_SECRET = 'CG4AfbyTy1YQmKiR6QyQUIW87o4u8XEDK5ctN7OBXWg9x'
CONSUMER_KEY = '4hXRlwa3gda7xO2lASh7tpilk'
CONSUMER_SECRET = 'SlWD9ArtYFi8HPzldyA8MpyCQRmXfeh7GhXW676QGHlEfgivcs'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

#class StreamListener(tweepy.StreamListener):

#    def on_status(self, status):
#        print(status.text)
        
#    def on_error(self, status_code):
#        if status_code == 420:
#            return False

#stream_listener = StreamListener()
#stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#stream.filter(track=["#NotreDame"],languages=["es"])


for status in tweepy.Cursor(api.home_timeline).items(100):
	print(status._json)

#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------