from http import client
from urllib import response
import tweepy
import pandas as pd
from pandas import json_normalize
import requests

ACCESS_TOKEN = "1138771862018711553-rsFeEOIvHxGd45GXLyvl0olOUVWHXi"
ACCESS_TOKEN_SECRET ="LLw5Dne0nyYLq3ESlMvW5WPmSAPX7VjGHCIXLdr6F7BhM"
CONSUMER_KEY ="t4r5sOx8PxT887edG2UkiYOrj"
CONSUMER_SECRET="guEeIRdGUsDUsYbagZwQ4l9dvbwlDGkC0aXJolf9IyWZITTeDc"
BEARER_TOKEN=F"AAAAAAAAAAAAAAAAAAAAAPX4fwEAAAAA4Xl%2F18Fu3Oi7nphn%2Fg5IfC%2BFWFs%3DLm8RFdcJNXENDhLckTxvdUc3RKcVFgt50NQNwRyEK8B8OiMoh3"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

query ='covid -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at','lang'], expansions=['author_id'] )

# 
#print(response)

# users = {u['id']: U for U in response.includes['users']}


# for tweet in response.data:
#     print(tweet.text)

j=response.json()

# df = json_normalize(response)

# print(df)