import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

pair = config.BTCUSDT

csvfile = open(pair + '-2017-2020-1mth.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')


candlesticks = client.get_historical_klines(pair, Client.KLINE_INTERVAL_1MONTH, "1 Jan, 2017")

for candlestick in candlesticks:
    candlestick[0] = int(candlestick[0] / 1000) # divide timestamp to ignore miliseconds
    print(candlestick[0])
    candlestick_writer.writerow(candlestick)


csvfile.close()