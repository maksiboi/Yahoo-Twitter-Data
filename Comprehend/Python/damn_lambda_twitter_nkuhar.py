import json
import boto3
import tweepy
import os

#ENVIRONMENT VARIALES

# access_token	        1568154686053572609-xzu2iScHZHq3yILZYDBngKxUTYa2ns
# access_token_secret	    DuGJgFHxJQHIDE0iltiInfN3KSbYoI179MwYofOQudMH1
# api_key	                g68pJcqHmM17CGz2o4gZDtIeR
# api_key_secret	        VA3wMnJ3NqCh2m3iYN6SlEbqDwnVop2wBknRcpbdCTcG8zjKR4


api_key = os.environ['api_key'] 
api_key_secret = os.environ['api_key_secret'] 

access_token = os.environ['access_token'] 
access_token_secret = os.environ['access_token_secret']

s3_client = boto3.client('s3')

S3_BUCKET = "damn-final-raw-bucket-test"
#BASE_DIR = "/temp"

def lambda_handler(event, context):
     
    #Authentification our account to twitter api
    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    #api instance
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    #Bitcoin (BTC)
    #Ethereum (ETH)
    #Binance Coin (BNB)
    #XRP (XRP)
    #Cardano (ADA)
    coin_names=["Cardano", "Ethereum", "Binance Coin", "XRP", "Bitcoin"]
    
    for n in coin_names:
        print(n)
        tweets = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#"'+n,count=50, include_entities=True, lang="en").items(100):
            tweets.append(tweet)

        for i in tweets:
            coin_name=n
            lista = i.entities["hashtags"]
            new_list = []
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                new_list.append(j["text"]) 
                    
    
            _json = {
                "coin_name" : coin_name,
                "created_at" : i.created_at.strftime("%m/%d/%Y", "%H:%M:%S"),
                "id" : i.id,
                "text" : i.text,
                "hashtags" : new_list,
                "retweet_count" : i.retweet_count,
                "user_id" : i.user.id,
                "user_followers_count" : i.user.followers_count,
                "user_friends_count" : i.user.friends_count
            }
            
            
            json_string = json.dumps(_json)
            json_bin = json_string.encode()
            
            response = s3_client.put_object( 
                Body = json_bin, 
                Bucket = S3_BUCKET, 
                Key="Twitter"+ "/" + "coin_name=" + coin_name + "/" + str(i.id) + ".json"
            )
            
    
