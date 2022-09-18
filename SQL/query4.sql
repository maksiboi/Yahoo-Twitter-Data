WITH max_tweets AS 
(
SELECT date_trunc('minute', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) as minutes,
        MAX(retweet_count) AS num_of_tweets
FROM comprehend
GROUP BY date_trunc('minute', date_parse(created_at, '%m/%d/%Y, %H:%i:%s'))
ORDER BY minutes
),
comprehend_grouped AS 
(
SELECT text,
        retweet_count, 
        date_trunc('minute', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')) AS minutes
FROM comprehend
GROUP BY date_trunc('minute', date_parse(created_at, '%m/%d/%Y, %H:%i:%s')), text, retweet_count
ORDER BY minutes
)
SELECT comprehend_grouped.text,
        max_tweets.minutes,
        max_tweets.num_of_tweets
FROM comprehend_grouped
RIGHT JOIN max_tweets ON
max_tweets.num_of_tweets = comprehend_grouped.retweet_count
GROUP BY max_tweets.minutes, comprehend_grouped.text, max_tweets.num_of_tweets
ORDER BY max_tweets.minutes