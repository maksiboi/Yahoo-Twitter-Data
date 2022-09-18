WITH nesto AS
(
    SELECT yfinance.high, 
    yfinance.low, 
    yfinance.open,
    yfinance.close, 
    yfinance.coin_name,
    twitter.retweet_count,
    twitter.id
    FROM yfinance
    JOIN twitter ON yfinance.coin_name = twitter.coin_name
    WHERE yfinance.coin_name = 'btc'
)

SELECT * FROM nesto
WHERE retweet_count IN (SELECT MAX(retweet_count) FROM nesto);