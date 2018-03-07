# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "nOeLxxfbiY7OVdWPOMily6OQP"
consumer_secret = "W3tQpKFZLCem4fkJb7DgyJTONUX6TwXIuImiFSi68O0qUM6T3o"
access_token = "457038348-W37pxbP3e2pxBpo9wagnRslwuaOcvFDp4y3GvKwu"
access_token_secret = "WH9Ex1WP76eAbIDGUjr4qRy0UFGxjq0jyhftWFRvfFImG"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
