# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:48:14 2020

@author: 33668
"""
import sys
sys.path.insert(0,'..')
import unittest
from utils import *

class TestMethods(unittest.TestCase):
    
    def test_load_model(self):
        model = load_model("model.pkl")
        self.assertEqual(len(model), 2)
        
    def test_process_tweet(self):
        tweet = '@issacb_ @Nike_Check_Mj On God! We gotta get him outta here!!!'
        words = process_tweet(tweet)
        self.assertEqual(words, ['god', 'gotta', 'get', 'outta'])
        
    def test_extract_features(self):
        theta,freqs = load_model("model.pkl")
        tweet = '@issacb_ @Nike_Check_Mj On God! We gotta get him outta here!!!'
        x = extract_features (tweet,freqs)
        self.assertEqual(np.sum(x),316.0)
        
    def test_sigmoid(self):
        self.assertEqual(sigmoid(0), 0.5)
    
    def test_predict_tweet(self):
        theta,freqs = load_model("model.pkl")
        tweet = '@mum, @dad, i am so happy to see you again!'
        self.assertGreater(predict_tweet(tweet,freqs,theta) ,0.5)
    
    def test_get_sentiment(self):
        model = load_model("model.pkl")
        tweets = ['@mum, @dad, i am so happy to see you again!', "OMG i hate you, i can't believe you can do this to me", '@mum, @dad, i am so happy to see you again!']
        sentiment = get_sentiment(tweets, model)
        self.assertEqual(sentiment , 1)
        
        model = load_model("model.pkl")
        tweets = ["OMG i hate you, i can't believe you can do this to me" , "OMG i hate you, i can't believe you can do this to me", '@mum, @dad, i am so happy to see you again!']
        sentiment = get_sentiment(tweets, model)
        self.assertEqual(sentiment , 0)
        
if __name__ == '__main__':
    unittest.main()