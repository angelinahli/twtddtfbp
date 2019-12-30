import os

import tweepy


consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = 'meganamram'

def get_tweets_by_ids(tweet_ids):
    return api.statuses_lookup(tweet_ids)

def get_tweets_until_id(until_id):
    # assume there will never be a 1000-tweet gap
    return api.user_timeline(username, since_id=until_id, count=1000)
