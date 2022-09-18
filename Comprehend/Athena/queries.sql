create schema damn_final

select * from twittertwitter limit 10

drop table twittertwitter

-- I want to get information on the highest and lowest price of a ticker in previous month 

CREATE TABLE IF NOT EXISTS h_l_ticker_per_month AS
    (SELECT strftime('%m', date) as previous_month,
        MAX(high) OVER (PARTITION BY CoinName ORDER BY CoinName) as highest_price,
        MIN(low) OVER (PARTITION BY CoinName ORDER BY CoinName) as lowest_price
    FROM yfinance_table
    WHERE previous_month = '%8')
    

-- I want to get information of the ticker with highest count of tweets in last 24 hours
    
    SELECT t.coin_name, y.Low, y.High,
        COUNT(id) OVER (PARTITION BY coin_name ORDER BY coin_name) AS num_of_tweets
    FROM twittertwitter as t
    INNER JOIN yfinance_table as y 
    ON t.coin_name = y.CoinName
    WHERE y.Date = current_date AS today_in_iso    -- today, not last 24h    
    

-- I want to get High, low, open, and close price for BTC ticker and a most popular tweet

    SELECT High, Low, Open, Close, CoinName, 
        

-- I want to get most popular tweet for the weeks in the previous month


-- I want to get the users who tweet most of each ticker

CREATE TABLE IF NOT EXISTS users_most_tweets AS
    (SELECT DISTINCT(user_id), coin_name,
        COUNT(coin_name) OVER (PARTITION BY user_id ORDER BY user_id asc) as number_of_tweets_per_ticker
    FROM twittertwitter)

SELECT * FROM users_most_tweets LIMIT 30

-- I want to get the percentage change in price on the highest and lowest prices for every 6 hours


-- I want to get the number of tweets for each ticker in 6 hours intervals



select created_at from twittertwitter limit 10