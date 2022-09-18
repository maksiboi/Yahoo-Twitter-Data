import yfinance as yf

btcData = yf.download(
                        start="2022-08-01",
                        end="2022-08-02",
                        tickers="ETH-USD",
                        interval="1h",
                        group_by="index"
                        )

btcData.drop('Volume', axis=1, inplace=True)
btcData.drop('Adj Close', axis=1, inplace=True)

btcData.index = btcData.index.strftime('%Y/%m/%d, %H:%M:%S')

btcData = btcData.T

with open('data.json', 'w') as f:
    f.write(btcData.to_json())
