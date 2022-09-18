-- 2. I want to get information of the ticker with highest count of tweets in last 24 hours

WITH num_tweets AS (
    SELECT
        t.coin_name, y.date, y.low, y.high,
        COUNT(id) OVER (PARTITION BY t.coin_name ORDER BY t.coin_name) AS num_of_tweets
    FROM
        twitter as t
        INNER JOIN yfinance as y ON t.coin_name = y.coin_name
    WHERE
        y.date LIKE '%-09-12%' --for 12.9.2022   
    )
    SELECT distinct(coin_name),
        MAX(num_of_tweets) OVER (PARTITION BY coin_name ORDER BY coin_name) as max_count
    FROM num_tweets