# Binance market order

#supertrend bot using python, pandas, and ccxt

https://ccxt.readthedocs.io/en/latest/manual.html
https://www.tradingfuel.com/supertrend-indicator-formula-and-calculation/
https://ccxt.readthedocs.io/en/latest/manual.html#exchanges

#supertrend definition:

#average true range

#true range=max[h-l,abs(h-c),abs(l-c)]
#atr mean of tr n stand for the time period setting

1. FIND THE BASIC UPPERBAND
   basic upperband = (h+l)/2 + k _ atr
   basic lowerband = (h+l)/2 - k _ atr

2. FIND THE FINAL UPPERBAND

#final upperband = if (currenent basic upperband < previous final upperband) & (Previous close < prviosus final lowerband>))

# Binance-Tradingview-bot

1. Tradingview webhook sent alert to the backend url which triggers the order
