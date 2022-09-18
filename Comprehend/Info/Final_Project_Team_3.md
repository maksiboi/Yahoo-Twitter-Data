# Final project

As an analyst, I need to be able to easily identify an analyze Twitter and Yahoo Finance data.
I need to access that data quickly in Athena without having to use additional operations.

- I want to get information on the highest and lowest price of a ticker in previous month 
- I want to get information of the ticker with highest count of tweets in last 24 hours
- I want to get High, low, open, and close price for BTC ticker and a most popular tweet
- I want to get most popular tweet for the weeks in the previous month
- I want to get the users who tweet most of each ticker
- I want to get the percentage change in price on the highest and lowest prices for every 6 hours
- I want to get the number of tweets for each ticker in 6 hours intervals

Extra:

- I want to get information on a ticker’s positivity using it’s price percentage change and it’s sentiment for every 6 hours 
    - If a ticker’s price percentage is positive and the sentiment is positive, mark as STRONG POSITIVE
    - If a ticker’s price percentage is positive and the sentiment is negative, mark as NEGATIVE
    - If a ticker’s price percentage is negative and the sentiment is positive, mark as POSITIVE
    - If a ticker’s price percentage is negative and the sentiment is negative, mark as STRONG NEGATIVE


**Data Source?**

* Yahoo Finance - https://github.com/ranaroussi/yfinance
* Twitter - https://developer.twitter.com/en/docs

**Target table schema matches the source schema?**

No

**Special handling required (i.e. hashing, obfuscation)?**

Yes – user names (Twitter) must be hashed

**Size of dataset?**

- yfinance: data from 2022-08-01 onwards (hourly interval)
- twitter: search for 500 tweets (search criteria: coin names, coin codes …)

**Target schema:**

1.	yfinance
    - Date (str, date)
    - Open (float)
    - Close (float)
    - High (float)
    - Low (float)
    - CoinName (str, custom)
2.	Twitter
    - coin_name (str, custom)
    - created_at (str, datetime)
    - id (int64)
    - text (str)
    - hashtags (str, unnest dictionary list into a plain list)
    - retweet_count (int)
    - user_id (int64)
    - user_followers_count (int)
    - user_friends_count(int)

**Acceptance criteria:**

- Code approved and merged to master
- Two tables: Yfinance and Twitter
- Twitter hashtags array is exploded into one column (hashtag / coin_name)
- Queries approved and pushed to master which answer the 7 points from the description.
- Ingestion deployed as IAC
- Extra: AWS Comprehend: add a SENTIMENT column to twitter dataset signifying the tweet’s sentiment

**Notes:**

- Use Twitter API v1.1 – research limitations and ensure your AWS services oblige
- Use DynamoDB to store information about latest loads (goal: incremental data load)
