import json
import boto3
import os
import yfinance as yf
from datetime import datetime, timedelta

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('damn-final-dynamodb-table-yfinance')

S3_BUCKET = "damn-final-raw-bucket"
BASE_DIR = "/tmp"

def get_data(ticker):

    datum = datetime.today()
    end = datum.strftime('%Y-%m-%d')
    start = (datum - timedelta(days=1)).strftime('%Y-%m-%d')

    coinData = yf.download(
                        start=start,
                        end=end,
                        tickers=ticker,
                        interval="1h"
                        )

    coinData.drop('Volume', axis=1, inplace=True)
    coinData.drop('Adj Close', axis=1, inplace=True)

    coinData.index = coinData.index.strftime('%Y-%m-%d, %H:%M:%S')

    coinData = coinData.T

    return coinData.to_json()



def lambda_handler(event, context):
    tickers = "ETH-USD BNB-USD XRP-USD ADA-USD BTC-USD"

    for ticker in tickers.split(' '):

        data = json.loads(get_data(ticker))

        for entry, attributes in data.items():

            date, time = entry.split(', ')

            dateTimeWrite = str(date) + "_" + str(time[:2])

            JSON_NAME = os.path.join(BASE_DIR, dateTimeWrite + ".json")

            if ticker == "ETH-USD":
                coin = "eth"
            elif ticker == "BNB-USD":
                coin = "bnb"
            elif ticker == "XRP-USD":
                coin = "xrp"
            elif ticker == "ADA-USD":
                coin = "ada"
            elif ticker == "BTC-USD":
                coin = "btc"

            content = {
                    "coin" : str(coin),
                    "date" : str(entry),
                    "open" : attributes['Open'],
                    "high" : attributes['High'],
                    "low" : attributes['Low'],
                    "close" : attributes['Close']
            }

            with open(JSON_NAME, 'w') as f:
                json.dump(content, f)

            s3_client.upload_file(JSON_NAME , S3_BUCKET, "yfinance/coin_name=" + coin + "/" + dateTimeWrite + ".json")

            contentDynamodb = {
                    "coin" : str(coin),
                    "date" : str(entry),
                    "open" : str(attributes['Open']),
                    "high" : str(attributes['High']),
                    "low" : str(attributes['Low']),
                    "close" : str(attributes['Close'])
            }

            table.put_item(Item=contentDynamodb)