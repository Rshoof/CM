import re

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set(words)

def load_tweets(file_path):
    with open(file_path, 'r') as file:
        tweets = file.read().splitlines()
    return tweets

def tokenize(tweet):
    tweet = re.sub(r"http\S+|@\S+|#\S+|[^a-zA-Z\s]", "", tweet)
    words = tweet.lower().split()
    return words

def sentiment_score(tweet, positive_words, negative_words):
    words = tokenize(tweet)
    score = sum(1 for word in words if word in positive_words) - sum(1 for word in words if word in negative_words)
    return score

positive_words = load_words('words_positive.txt')
negative_words = load_words('words_negative.txt')
tweets = load_tweets('tweets.txt')

tweets_with_scores = [(tweet, sentiment_score(tweet, positive_words, negative_words)) for tweet in tweets]

sorted_tweets = sorted(tweets_with_scores, key=lambda x: x[1], reverse=True)

for tweet, score in sorted_tweets:
    print(f"Score: {score} | Tweet: {tweet}")

