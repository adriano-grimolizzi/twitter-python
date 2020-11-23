# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:25:50 2020

@author: 33668
"""

import re
import string
import numpy as np
import pickle

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

def load_model(filename):
    """ Load pre-trained ML model"""
    
    with open(filename, 'rb') as f:  # Python 3: open(..., 'rb')
        theta, freqs = pickle.load(f)
    return theta, freqs

def process_tweet(tweet):
    """ remove unimportant information in the tweet like URLs, 
    special characters, retweet symbols..."""
    
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
        
    # remove hyperlinks, symbols, hashtags, punctuation
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    
    # =============================================================================
    #     truncate word to stem
    # =============================================================================
        
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)
    keep = []
    for word in tweet_tokens:
        if word not in string.punctuation and word not in stopwords_english:
            keep.append(word)
            
    return keep

def extract_features(tweet, freqs):
    '''
    Input: 
        tweet: a list of words for one tweet
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
    Output: 
        x: a feature vector of dimension (1,3)
    '''
    # process_tweet tokenizes, stems, and removes stopwords
    word_l = process_tweet(tweet)
    
    # 3 elements in the form of a 1 x 3 vector
    x = np.zeros((1, 3)) 
    
    #bias term is set to 1
    x[0,0] = 1 
      
    # loop through each word in the list of words
    for word in word_l:
        
        # increment the word count for the positive label 1
        x[0,1] += freqs.get((word, 1.0),0)
        
        # increment the word count for the negative label 0
        x[0,2] += freqs.get((word, 0.0),0)
        
    assert(x.shape == (1, 3))
    return x

def sigmoid(z): 
    '''
    Input:
        z: is the input (can be a scalar or an array)
    Output:
        h: the sigmoid of z
    '''
    # calculate the sigmoid of z
    h = 1/(1+np.exp(-z))
    
    return h


def predict_tweet(tweet, freqs, theta):
    '''
    Input: 
        tweet: a string
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
        theta: (3,1) vector of weights
    Output: 
        y_pred: the probability of a tweet being positive or negative
    '''

    # extract the features of the tweet and store it into x
    x = extract_features(tweet,freqs)
    
    # make the prediction using x and theta
    y_pred = sigmoid(x.dot(theta))

    return y_pred

def get_sentiment(tweets, model):
    predictions = []
    theta, freqs = model
    for tweet in tweets:
        predictions.append(predict_tweet(tweet, freqs, theta)[0][0]>0.5)
        
    return  round(sum(predictions)/len(predictions))
    

    