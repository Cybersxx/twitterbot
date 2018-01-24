from credentials import *
from time import sleep
import sys
import tweepy
import markovify
from random import randint
#from corpus_creator import *

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(auth)

with open("corpus.txt") as corpus_file:
	corpus_a = corpus_file.read()

with open("corpus2.txt") as corpus_file:
	corpus_b = corpus_file.read()

model_a = markovify.Text(corpus_a)
model_b = markovify.Text(corpus_b)
model_combo = markovify.combine([ model_a, model_b ], [ 10, 100 ])

keywords = ['league',
            'legends',
            'league of legends',
            'lol',]


def follow_people():
    for tweet in tweepy.Cursor(api.search, q='#leagueoflegends', lang='en').items(10):
        try:
            tweet.user.follow()
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(900)
            continue
        except StopIteration:
            break
    for follower in tweepy.Cursor(api.followers).items():
        try:
            follower.follow()
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(900)
            continue
        except StopIteration:
            break
def post_status():
    sen=model_combo.make_short_sentence(140)
    print (sen)
    api.update_status(sen)
    sleep(60)


def reply_people():
    print("reply to people")
    for tweet in tweepy.Cursor(api.search, q='#leagueoflegends', lang='en').items(1) :
        try:
            sn=tweet.user.screen_name
            sen= model_combo.make_short_sentence(140)
            m="@%s " % (sn) + sen
            print(m)
            api.update_status(m, tweet.id)
            sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(900)
            continue
        except StopIteration:
            break

def main():
    while True:
        try:
            follow_people()
            x= randint(1,9)
            print(x)
            if x>2:
                post_status()
            else:
                reply_people()
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(900)
            continue
        except StopIteration:
            break

if __name__ == "__main__": main()
