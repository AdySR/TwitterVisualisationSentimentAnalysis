from ast import keyword
from cgitb import text
from multiprocessing.connection import Listener
from operator import truediv
from os import access
from tweepy.streaming import Stream
from tweepy import OAuthHandler
import twitter_credentials

class Listener(Stream):

    def on_status(self, status):
        print(status.user.screen_name + ":"+status.text)

ACCESS_TOKEN = "1138771862018711553-rsFeEOIvHxGd45GXLyvl0olOUVWHXi"
ACCESS_TOKEN_SECRET ="LLw5Dne0nyYLq3ESlMvW5WPmSAPX7VjGHCIXLdr6F7BhM"
CONSUMER_KEY ="t4r5sOx8PxT887edG2UkiYOrj"
CONSUMER_SECRET="guEeIRdGUsDUsYbagZwQ4l9dvbwlDGkC0aXJolf9IyWZITTeDc"

stream_tweet = Listener(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

keyword= ['2022','#python']

stream_tweet.filter(track=keyword)