SELECT date_trunc('day', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) + 
        floor(extract(hour FROM date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) / 6.0) * 6 * interval '1' hour AS date_interval,
        coin_name, 
        COUNT(*) AS number_of_tweets
FROM twitter
GROUP BY date_trunc('day', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) + 
        floor(extract(hour FROM date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) / 6.0) * 6 * interval '1' hour, coin_name
ORDER BY coin_name, date_interval