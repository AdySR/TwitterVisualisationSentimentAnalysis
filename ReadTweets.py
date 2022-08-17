from http import client
from itertools import count
from logging import exception
from urllib import response
import tweepy
import pandas as pd
from pandas import json_normalize
import requests
from explode_tweets import explode_tweets

ACCESS_TOKEN = "1138771862018711553-rsFeEOIvHxGd45GXLyvl0olOUVWHXi"
ACCESS_TOKEN_SECRET ="LLw5Dne0nyYLq3ESlMvW5WPmSAPX7VjGHCIXLdr6F7BhM"
CONSUMER_KEY ="t4r5sOx8PxT887edG2UkiYOrj"
CONSUMER_SECRET="guEeIRdGUsDUsYbagZwQ4l9dvbwlDGkC0aXJolf9IyWZITTeDc"
BEARER_TOKEN=F"AAAAAAAAAAAAAAAAAAAAAPX4fwEAAAAA4Xl%2F18Fu3Oi7nphn%2Fg5IfC%2BFWFs%3DLm8RFdcJNXENDhLckTxvdUc3RKcVFgt50NQNwRyEK8B8OiMoh3"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

query ='#centricconsulting -is:retweet'

response = client.search_recent_tweets(query=query, max_results=50, tweet_fields=['created_at','lang'], expansions=['author_id'] )

print(response)

try:
    if (response.data)==None:
        print("Empty response. Exception block begin >>")

    tweet_text=[]
    for tweet in response.data:
        tweet_text.append(tweet)

    else:
        print(".. processing the query to DF")
        df_raw_tweet = pd.DataFrame(tweet_text)
        df_raw_tweet.to_csv('recent_tweets.csv')

except:
    print(""" >> Check the API query.
              >> Else check the output file if its already opened   """)
