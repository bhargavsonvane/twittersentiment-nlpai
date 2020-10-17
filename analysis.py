
import tweepy
import os
import json
from datetime import datetime, timedelta
import re
from nltk.tokenize import WordPunctTokenizer
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# We access the access codes to our Twitter App:
with open('Keys.json') as f:
    data = json.load(f)

ACC_TOKEN = data["Access_token"]
ACC_SECRET = data["Access_token secret"]
CONS_KEY = data["API_key"]
CONS_SECRET = data["API_secret key"]


def authentication(cons_key, cons_secret, acc_token, acc_secret):
    """
    Function to get access to a Twitter app given the
    keys.

    Args:
        cons_key: Consumer Key.
        cons_secret: Consumer API Secret.
        acc_token: Access Token.
        acc_secret: Access Token Secret.

    Returns:
        api with guaranteed access.
    """

    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)

    return api


def search_tweets(keyword, total_tweets):
    """
    Function to search for tweets in English given a keyword and a total number of tweets. In
    in this case they are also limited to searching in a period no longer than 24 hours.

    Args:
        keyword: Word to search on Twitter.
        total_tweets: Total number of tweets to search.

    Returns:
        search result: Iterable with all the information of the tweets found.
    """

    today_datetime = datetime.today().now()
    yesterday_datetime = today_datetime - timedelta(days=1)
    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
    api = authentication(CONS_KEY, CONS_SECRET, ACC_TOKEN, ACC_SECRET)
    search_result = tweepy.Cursor(api.search,
                                  q=keyword,
                                  since=yesterday_date,
                                  result_type='recent',
                                  lang='es').items(total_tweets)

    return search_result


def clean_tweets(tweet):
    """
    Function to clean tweets before they are sent to the analysis API
    sentiments.

    Note:   The Google Cloud Natural Language API is quite flexible when it comes to performing analysis of
            sentiments.. I'm not sure all these "cleanings" are at all
            necessary.

    Args:
        tweet: Tweet (the text) to clear.

    Returns:
        clean_tweet: Tweet already clean to proceed with sentiment analysis.
    """

    # We remove the user in the tweet
    user_removed = re.sub(r'@[A-Za-z0-9]+', '', tweet.decode('utf-8'))

    # We remove any link present in the tweet
    link_removed = re.sub('https?://[A-Za-z0-9./]+', '', user_removed)

    # we take everything to lowercase
    lower_case_tweet = link_removed.lower()

    # We instantiate a tokenizer and, according to its rules, create the list of tokens
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)

    # We join the tokens to create a single string to be sent
    clean_tweet = (' '.join(words)).strip()

    return clean_tweet


def get_sentiment_score(tweet):
    """
    Function used by Google's NLP API to perform sentiment analysis
    about a text.

    Args:
        tweet: Tweet (or text) to perform sentiment analysis.

    Returns:
        sentiment_score: Sentiment score ranging from -1.0 (negative) to
        
1.0 (positive).

    Note:
        Google's sentiment analysis also returns a magnitude value ("magnitude").
        This value is used to determine the overall "strength" of the calculated sentiment. For
        more detail consult:
            https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
    """

    client = language.LanguageServiceClient()
    document = types\
        .Document(content=tweet, type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
        .analyze_sentiment(document=document)\
        .document_sentiment\
        .score

    return sentiment_score


def analyze_tweets(keyword, total_tweets):
    """
    General function to perform the analysis of tweets, includes the previous functions.

    Args:
        keyword: 
Word to search on Twitter.
        total_tweets: Total number of tweets to search

    Returns:
        final_score: 
Average of the sentiment score among the analyzed tweets.
    """

    score = 0
    tweets = search_tweets(keyword, total_tweets)
    lista_tweets = []
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        no_link_tweet = re.sub('https?://[A-Za-z0-9./]+', '', tweet.text)
        lista_tweets.append((no_link_tweet, sentiment_score))
    final_score = round((score / float(total_tweets)), 2)

    return final_score, lista_tweets


# Example Cases:

# 1.- Testing specific comments:
""" bad_comment = get_sentiment_score('¡This washing machine is useless!')
good_comment = get_sentiment_score('This washing machine is great')
neutral_comment = get_sentiment_score('Washer but the least')

print('bad_comment_score:', bad_comment)
print('good_comment_score:', good_comment)
print('neutral_comment_score:', neutral_comment) """
