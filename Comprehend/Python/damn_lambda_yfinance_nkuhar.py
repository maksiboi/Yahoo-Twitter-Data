
import json
import boto3
import os
import yfinance as yf
import pandas as pd


s3_client = boto3.client('s3')

S3_BUCKET = "damn-final-raw-bucket"
BASE_DIR = "/tmp"

def get_data(tickers=['ETH-USD', 'BNB-USD', 'XRP-USD', 'ADA-USD']):
    for ticker in tickers:
        btcData = yf.download(
                        start="2022-08-01",
                        end="2022-08-12",
                        tickers=ticker,
                        interval="1h"
                        )

        btcData.drop('Volume', axis=1, inplace=True)
        btcData.drop('Adj Close', axis=1, inplace=True)

        btcData['Date'] = btcData.index.strftime('%Y/%m/%d, %H:%M:%S')
        btcData['coin'] = ticker
        break

    return pd.concat([btcData])



def lambda_handler(event, context):

    data = json.loads(get_data())

    fileNumber = 0
    for attCoi, entries in data.items():
        fileNumber += 1
    
        attCoi = attCoi.replace("'", "")
        attCoi = attCoi.replace("(", "")
        attCoi = attCoi.replace(")", "")
        attribute, coin = attCoi.split(', ')

        JSON_NAME = os.path.join(BASE_DIR, str(fileNumber) + ".json")

        with open(JSON_NAME, 'w') as f:
            content = {
                "attribute" : attribute,
                "coin" : coin,
                "data" : entries
            }
            json.dump(content, f)

        s3_client.upload_file(JSON_NAME , S3_BUCKET, "yfinance/coin=" + coin + "/" + str(fileNumber) + ".json")