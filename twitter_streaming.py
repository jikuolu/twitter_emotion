# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:46:33 2016

@author: Jikuo
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "360765346-nOaYz42uLZc0Hvn33EQS0DabV4ifZ3n62v8W983M"
access_token_secret = "MTrVRTp6oaTi1r0qTbhQIRINFfehZo32hLkoiKhT00rn1"
consumer_key = "TEi0UV4WvPrmzD0nhHdrhkgaN"
consumer_secret = "iUOC4g8JIs9VO8Il2lLtglun2KgzL4dr3GH0lm1vV4062fH0MK"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        with open('fetched_tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status
        
          
posifaces = [u"\U0001F601", u"\U0001F602", u",\U0001F603",u"\U0001F604",\
             u"\U0001F605",u"\U0001F606",u"\U0001F609",u"\U0001F60A",\
             u"\U0001F60B",u"\U0001F60C"]
negafaces = [u"\U0001F621",u"\U0001F622",u"\U0001F623",u"\U0001F624",\
             u"\U0001F62D","anger","angry"]
emotions = posifaces + negafaces
#emotions = negafaces
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track= [''.join(Emoticons.POSITIVE), ''.join(Emoticons.NEGATIVE)],languages = ["en"])
    stream.filter(track= emotions)