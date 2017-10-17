from twitterscraper import query_tweets

for tweet in query_tweets("Trump", 10)[:10]:
	print(tweet.text)

