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

ACCESS_TOKEN = "1138771862018711553-XMSkK6gGnMviaVRJ8zX3OcgfJcWNZA"
ACCESS_TOKEN_SECRET ="3eYMZ58BrpTBAPqKDBxdzrhviSVOcpNP8j5lgRj4I67Yo"
CONSUMER_KEY ="zOZhCaV3HmGYH47O1HQrfvynm"
CONSUMER_SECRET="5gZbFZIsDW1SvFxaLrawKl2bp8TisGjDFmPrjC6CNtbh7CTHUP"

stream_tweet = Listener(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

keyword= ['2022','#python']

stream_tweet.filter(track=keyword)
