import pandas as pd
from explode_tweets import explode_tweets
from select_text import select_text

# flatten tweets
tweets = explode_tweets(tweets_data)

# select text
tweets = select_text(tweets)
columns = ['text', 'lang', 'user-location', 'place-country', 
           'place-country_code', 'location-coordinates', 
           'user-screen_name']

# Create a DataFrame from `tweets`
df_tweets = pd.DataFrame(tweets, columns=columns)
# replaces NaNs by Nones
df_tweets.where(pd.notnull(df_tweets), None, inplace=True)