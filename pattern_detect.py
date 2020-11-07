import talib
import yfinance as yf

data = yf.download("SPY", start="2020-01-01", end="2020-08-01")
print(data)