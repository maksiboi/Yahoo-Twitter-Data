CREATE TABLE IF NOT EXISTS additionalTask AS
(
WITH combined_tables AS 
(
SELECT max_sentiments_per6h.date_interval AS date_interval, 
        max_sentiments_per6h.coin_name AS coin_name, 
        percentage_diffs_per6h.high_percentage_change AS percentage_change, 
        max_sentiments_per6h.sentiment AS sentiment
FROM max_sentiments_per6h
LEFT JOIN percentage_diffs_per6h ON
max_sentiments_per6h.date_interval = percentage_diffs_per6h.date_interval
AND 
max_sentiments_per6h.coin_name = percentage_diffs_per6h.coin_name
)
SELECT date_interval, 
        coin_name, 
        percentage_change, 
        sentiment,
        (CASE 
            WHEN percentage_change > 0 AND sentiment = 'POSITIVE' THEN 'STRONG POSITIVE'
            WHEN percentage_change > 0 AND sentiment = 'NEGATIVE' THEN 'NEGATIVE'
            WHEN percentage_change < 0 AND sentiment = 'POSITIVE' THEN 'POSITIVE'
            WHEN percentage_change < 0 AND sentiment = 'NEGATIVE' THEN 'STRONG NEGATIVE'
        END) AS positivity
FROM combined_tables
)