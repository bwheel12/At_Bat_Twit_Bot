from twython import Twython
import requests, json
from bs4 import BeautifulSoup
import re, random
import pandas as pd


with open('../Twitter_Keys/APP_KEY') as f:
    APP_KEY = f.readlines()
APP_KEY = APP_KEY[0].strip()

with open('../Twitter_Keys/APP_SECRET') as f:
    APP_SECRET = f.readlines()
APP_SECRET = APP_SECRET[0].strip()

with open('../Twitter_Keys/OAUTH_TOKEN') as f:
    OAUTH_TOKEN = f.readlines()
OAUTH_TOKEN = OAUTH_TOKEN[0].strip()

with open('../Twitter_Keys/OAUTH_SECRET') as f:
    OAUTH_TOKEN_SECRET = f.readlines()
OAUTH_TOKEN_SECRET = OAUTH_TOKEN_SECRET[0].strip()


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_stat_cast_winner():
    statcast_table = pd.read_csv('./Todays_statcast.csv')
    hardest_hit_row = statcast_table['launch_speed'].idxmax()
    player = statcast_table.loc[hardest_hit_row,'player_name']
    comma  = player.find(',')
    player = player[comma+1:] + ' ' + player[:comma]
    velo   = statcast_table.loc[hardest_hit_row,'launch_speed']
    date   = statcast_table.loc[hardest_hit_row,'game_date']
    
    return player, velo, date
    

def postOnTwitter():
    player, velo, date = get_stat_cast_winner()
    tweet_string = player + " had the hardest hit ball on " + date + " in MLB with an exit velo of " + str(velo) + " mph. I am the at bat bot. This action was performed automatically."
    print(tweet_string)
    twitter.update_status(status=tweet_string)
    
postOnTwitter()
