from twitterscraper import query_tweets
import eval
import sys
import numpy as np


def formatText(text):
    text = text.encode('utf-8', errors='ignore')
    return text.decode('utf-8')


if __name__ == "__main__":
    tweets = []
    print('Running Eval...')

    for tweet in query_tweets("Trump", 100)[:100]:
        tweets.append(format(tweet.text))

    eval.runAnalysis(tweets)
