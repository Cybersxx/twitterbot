from credentials import *
import praw
import pprint
from praw.models import MoreComments
import sys

reddit= praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent = reddit_username)

sys.stdout = open('corpus2.txt','wt' )

def create_corpus():
    for submission in reddit.subreddit('leagueoflegends').hot(limit=100):
        print(submission.title)

        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            print(top_level_comment.body)

def main():
    create_corpus()

if __name__ == "__main__": main()
