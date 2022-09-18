WITH podijeljeno AS (
    SELECT date_trunc('day', date_parse(date, '%Y-%m-%d, %H:%i:%s')) + 
            floor(extract(hour FROM date_parse(date, '%Y-%m-%d, %H:%i:%s')) / 6.0) * 6 * interval '1' hour AS date_interval,
           MAX(high) AS high, 
           MIN(low) AS low,
           coin_name
    FROM yfinance
    GROUP BY date_trunc('day', date_parse(date, '%Y-%m-%d, %H:%i:%s')) + 
            floor(extract(hour FROM date_parse(date, '%Y-%m-%d, %H:%i:%s')) / 6.0) * 6 * interval '1' hour, coin_name
    ORDER BY coin_name, date_interval
),
dodan_lag AS (
    SELECT date_interval,
    high,
    low,
    LAG(high) OVER (ORDER BY coin_name, date_interval) AS last_high,
    LAG(low) OVER (ORDER BY coin_name, date_interval) AS last_low,
    coin_name
    FROM podijeljeno
    ORDER BY coin_name, date_interval
)
SELECT date_interval,
    high,
    low,
    (high / last_high - 1) * 100 AS high_percentage_change,
    (low / last_low - 1) * 100 AS low_percentage_change,
    coin_name
FROM dodan_lag