import json
import os

S3_BUCKET = "damn-final-raw-bucket"
BASE_DIR = "/tmp"

with open('data.json', 'r') as f:
    data = json.load(f)

for attCoi, entries in data.items():
    
    attCoi = attCoi.replace("'", "")
    attCoi = attCoi.replace("(", "")
    attCoi = attCoi.replace(")", "")
    attribute, coin = attCoi.split(', ')

    for dateHour, value in entries.items():

        hour = dateHour[-2:]
        date = dateHour[:-4]

        y, m, d = date.split('/')
        
        JSON_NAME = os.path.join(BASE_DIR, hour + ".json")

        with open(JSON_NAME, 'w') as f:
            json.dump({"value" : value}, f)

        print("yfinance/coin=" + coin + "/year=" + y + "/month=" + m + "/day=" + d + "/attribute=" + attribute + "/" + hour + ".json")