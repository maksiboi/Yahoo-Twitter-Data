-- I want to get the users who tweet most of each ticker

SELECT user_id, coin_name, user_tweet_count_per_coin
FROM
(
    WITH counted_over_departments AS (
    SELECT user_id, coin_name,
    COUNT(user_id) OVER (PARTITION BY coin_name ORDER BY user_id) AS user_tweet_count_per_coin
    FROM twitter
    WHERE user_id IS NOT NULL OR user_id = ''
    ORDER BY user_tweet_count_per_coin DESC
    )
SELECT user_id, coin_name, user_tweet_count_per_coin,
row_number() OVER(PARTITION BY coin_name ORDER BY user_tweet_count_per_coin DESC) as pop_rank
FROM counted_over_departments
)
WHERE pop_rank = 1
ORDER BY coin_name