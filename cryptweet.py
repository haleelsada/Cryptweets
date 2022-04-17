import tweepy
import json
import emoji
import transformers
from transformers import pipeline

sentimentmodel=pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")



# authenticate the api key and token with twitter

from tweepy.auth import OAuthHandler

auth = OAuthHandler('t6d8uj4w9P6DjrNSmfSd42gEI', 'ZLcVXunCbN6NO4rUup6vTR33rO32epm0LFHLkzFLZnhjbQmQzZ')
auth.set_access_token('1405483945379074054-ktOMmQ6HUcZwzOxiHfjcFmP74hkTn5', 'hV792qfEAuJcvZmkzmoMf61qaaSnoV8D2YiIFYjzAgr06')


api = tweepy.API(auth,wait_on_rate_limit=True)


# extract the tweets with the given keyword

def tweextractor(keyword):

  tweet=[]      #list to store tweets extracted
 
  # search_tweets method extract atmost 100 tweets with given keyword
  # use it with cursor to extract more than that in one go
  
  # take 500 popular tweets and 500 recent tweets to keep consistency in the result

  for i in tweepy.Cursor(api.search_tweets, keyword,tweet_mode="extended",lang='en',result_type='recent',count=100).items(500):
    i = json.dumps(i._json)
    i = json.loads(i)
    if i['full_text'] not in tweet and len(i['full_text'])<400:
      tweet.append(i['full_text'])
  for i in tweepy.Cursor(api.search_tweets, keyword,tweet_mode="extended",lang='en',result_type='popular',count=100).items(500):
    i = json.dumps(i._json)
    i = json.loads(i)
    if i['full_text'] not in tweet and len(i['full_text'])<400:
      tweet.append(i['full_text'])
  print(len(tweet),'tweets total tweets found')
  return tweet
  


# method to take keyword and find overall sentiment

def sentimentanalyser(keyword):
  tweets=tweextractor(keyword)
  score=[]
  mood=sentimentmodel(tweets)
  for i in mood:
    if i['label']=='POS':
      score.append(i['score'])
    elif i['label']=='NEG':
      score.append(-i['score'])
  sentiment=sum(score)/len(score)
  if sentiment>0:
    return 'Sentiment of public is positive with probability '+str(sentiment)
  else:return 'Sentiment of public is negative with probability '+str(-sentiment)


