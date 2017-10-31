from twitterscraper import query_tweets
import eval
import argparse
import sys
import numpy as np


def formatText(text):
    text = text.encode('utf-8', errors='ignore')
    return text.decode('utf-8')

def parseArguments():
    parser = argparse.ArgumentParser(description='Analyze Tweets')
    parser.add_argument('integers', type=int,
                        help='number of tweets to include in analysis')
    parser.add_argument('hashtag', type=str,
                        help='the string to query on')

    args = parser.parse_args()
    return(args.integers, args.hashtag)


if __name__ == "__main__":
    tweets = []
    print('Running Eval...\n')
    number, hashtag = parseArguments()

    for tweet in query_tweets(hashtag, number)[:number]:
        tweets.append(format(tweet.text))

    # y_test = np.full(len(tweets), 1)

    twitterAnalysis = eval.TwitterAnalysis(tweets, hashtag)
    twitterAnalysis.runAnalysis()

