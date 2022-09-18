CREATE TABLE IF NOT EXISTS max_sentiments_per6h AS
(
WITH numbers_of_sentiment AS 
(
SELECT date_trunc('day', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) + 
        floor(extract(hour FROM date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) / 6.0) * 6 * interval '1' hour AS date_interval,
        coin_name,
        COUNT(sentiment) AS num_of_sent, 
        sentiment
FROM sentimentcomprehend
GROUP BY date_trunc('day', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) + 
        floor(extract(hour FROM date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) / 6.0) * 6 * interval '1' hour, coin_name, sentiment
ORDER BY coin_name, date_interval
),
max_sent AS 
(
SELECT  coin_name, 
        MAX(num_of_sent) AS num_of_sent
FROM numbers_of_sentiment
WHERE sentiment != 'NEUTRAL'
GROUP BY coin_name
)
SELECT numbers_of_sentiment.date_interval, 
        numbers_of_sentiment.coin_name, 
        numbers_of_sentiment.num_of_sent,
        numbers_of_sentiment.sentiment
FROM numbers_of_sentiment
JOIN max_sent ON
numbers_of_sentiment.num_of_sent = max_sent.num_of_sent
)