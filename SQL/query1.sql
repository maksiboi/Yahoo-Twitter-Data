-- 1. I want to get information on the highest and lowest price of a ticker in previous month 
CREATE TABLE IF NOT EXISTS h_l_ticker_price_per_previous_month AS (
    SELECT
        highest_price,
        lowest_price,
        coin_name,
        min_rank,
        max_rank
    FROM
        (
            WITH max_min_coin AS (
                SELECT
                    coin_name,
                    MAX(high) OVER (
                        PARTITION BY coin_name
                        ORDER BY
                            coin_name
                    ) as highest_price,
                    MIN(low) OVER (
                        PARTITION BY coin_name
                        ORDER BY
                            coin_name
                    ) as lowest_price
                FROM
                    yfinance
                WHERE
                    date like '%-08-%'
            )
            SELECT
                highest_price,
                lowest_price,
                coin_name,
                row_number() OVER (
                    PARTITION BY coin_name
                    ORDER BY
                        highest_price DESC
                ) as max_rank,
                row_number() OVER (
                    PARTITION BY coin_name
                    ORDER BY
                        lowest_price ASC
                ) as min_rank
            FROM
                max_min_coin
        )
    WHERE
        max_rank = 1
        and min_rank = 1
)