import json
import boto3
import tweepy
import os
import boto3

api_key = os.environ(api_key)
api_key_secret = os.environ(api_key_secret)

access_token = os.environ(access_token)
access_token_secret = os.environ(access_token_secret)

s3_client = boto3.client('s3')

S3_BUCKET = "damn-final-raw-bucket"
BASE_DIR = "/tmp"

def lambda_handler(evet, context):
    
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
    
    try:
        #CARDANO
        tweets_cardano = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#Cardano"',count=50, include_entities=True, lang="en").items(100):
            tweets_cardano.append(tweet)
        
        for i in tweets_cardano:
            coin_name="ada"
            lista = i.entities["hashtags"]
            pom=""
            brojac = 0
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                if(brojac == len(lista)-1):
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) 
                else:
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) +", " 
                brojac+=1
        
            cardano_json= {
                "coin_name" : coin_name,
                "created_at" : i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                "id" : i.id,
                "text" : i.text,
                "hashtags" : pom,
                "retweet_count" : i.retweet_count,
                "user_id" : i.user.id,
                "user_followers_count" : i.user.followers_count,
                "user_friends_count" : i.user.friends_count
            }
            JSON_NAME = os.path.join(BASE_DIR, str(i.id) + ".json")
            with open(JSON_NAME, 'w') as f:
                        json.dump(cardano_json, f)
            s3_client.upload_file(JSON_NAME , S3_BUCKET,"Twitter" +"/" + "coin_name=" + coin_name + "/" + str(i.id) + ".json")
            
        #XRP
        tweets_xrp = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#XRP"',count=50, include_entities=True, lang="en").items(100):
                tweets_xrp.append(tweet)
            
        
        for i in tweets_xrp:
            coin_name="xrp"
            lista = i.entities["hashtags"]
            pom=""
            brojac = 0
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                if(brojac == len(lista)-1):
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) 
                else:
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) +", " 
                brojac+=1
            
            xrp_json= {
                    "coin_name" :coin_name,
                    "created_at" : i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    "id" : i.id,
                    "text" : i.text,
                    "hashtags" : pom,
                    "retweet_count" : i.retweet_count,
                    "user_id" : i.user.id,
                    "user_followers_count" : i.user.followers_count,
                    "user_friends_count" : i.user.friends_count
            }
            JSON_NAME = os.path.join(BASE_DIR, str(i.id) + ".json")
            with open(JSON_NAME, 'w') as f:
                        json.dump(xrp_json, f)
            s3_client.upload_file(JSON_NAME , S3_BUCKET,"Twitter" +"/" + "coin_name=" + coin_name + "/" + str(i.id) + ".json")
         
        #Binance Coin     
        tweets_binance = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#Binance Coin"',count=50, include_entities=True, lang="en").items(100):
            tweets_binance.append(tweet)

    
        for i in tweets_binance:
            coin_name="bnb"
            lista = i.entities["hashtags"]
            pom=""
            brojac = 0
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                if(brojac == len(lista)-1):
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) 
                else:
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) +", " 
                brojac+=1
            
            bnb_json= {
                    "coin_name" : coin_name,
                    "created_at" : i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    "id" : i.id,
                    "text" : i.text,
                    "hashtags" : pom,
                    "retweet_count" : i.retweet_count,
                    "user_id" : i.user.id,
                    "user_followers_count" : i.user.followers_count,
                    "user_friends_count" : i.user.friends_count
            }
            JSON_NAME = os.path.join(BASE_DIR, str(i.id) + ".json")
            with open(JSON_NAME, 'w') as f:
                        json.dump(bnb_json, f)
            s3_client.upload_file(JSON_NAME , S3_BUCKET,"Twitter"+"/"+ "coin_name=" + coin_name + "/" + str(i.id) + ".json")
            
        #Etherium
        tweets_eth = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#Ethereum"',count=50, include_entities=True, lang="en").items(100):
            tweets_eth.append(tweet)


        for i in tweets_eth:
            coin_name="eth"
            lista = i.entities["hashtags"]
            pom=""
            brojac = 0
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                if(brojac == len(lista)-1):
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) 
                else:
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) +", " 
                brojac+=1
            
            eth_json= {
                    "coin_name" : coin_name,
                    "created_at" : i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    "id" : i.id,
                    "text" : i.text,
                    "hashtags" : pom,
                    "retweet_count" : i.retweet_count,
                    "user_id" : i.user.id,
                    "user_followers_count" : i.user.followers_count,
                    "user_friends_count" : i.user.friends_count
            }
            JSON_NAME = os.path.join(BASE_DIR, str(i.id) + ".json")
            with open(JSON_NAME, 'w') as f:
                        json.dump(eth_json, f)
            s3_client.upload_file(JSON_NAME , S3_BUCKET,"Twitter" +"/" + "coin_name=" + coin_name + "/" + str(i.id) + ".json")
        
        #Bitcoin
        tweets_bit = []
        for tweet in tweepy.Cursor(api.search_tweets, q='"#Bitcoin"',count=50, include_entities=True, lang="en").items(100):
            tweets_bit.append(tweet)
        
        for i in tweets_bit:
            coin_name="btc"
            lista = i.entities["hashtags"]
            pom=""
            brojac = 0
            #hashtags (str, unnest dictionary list into a plain list)
            for j in lista:
                if(brojac == len(lista)-1):
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) 
                else:
                    pom+="text : "+j["text"] + ", indices: " + str(j["indices"]) +", " 
                brojac+=1
            
            btc_json= {
                    "coin_name" : coin_name,
                    "created_at" : i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    "id" : i.id,
                    "text" : i.text,
                    "hashtags" : pom,
                    "retweet_count" : i.retweet_count,
                    "user_id" : i.user.id,
                    "user_followers_count" : i.user.followers_count,
                    "user_friends_count" : i.user.friends_count
            }
            JSON_NAME = os.path.join(BASE_DIR, str(i.id) + ".json")
            with open(JSON_NAME, 'w') as f:
                        json.dump(btc_json, f)
            s3_client.upload_file(JSON_NAME , S3_BUCKET,"Twitter" +"/" + "coin_name=" + coin_name + "/" + str(i.id) + ".json")
            
        
    except Exception:
        return Exception