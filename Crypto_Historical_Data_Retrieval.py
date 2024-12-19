import requests
import pandas as pd
import numpy as np


url = "https://min-api.cryptocompare.com/data/v2/histoday"
params = {
    "fsym": "BTC",       # Cryptocurrency symbol (e.g., BTC for Bitcoin)
    "tsym": "USD",       # Target currency (e.g., USD)
    "limit": 365,        # Number of days (e.g., last 365 days)
    "api_key": "31e4c1d445934de5a1aa6618a4c12c60fd49329298309ea0e197b8eca292527d"  
}


response = requests.get(url, params=params)


data = response.json()["Data"]["Data"]


df = pd.DataFrame(data)


df["time"] = pd.to_datetime(df["time"], unit="s")
print(df[["time", "open", "high", "low", "close"]])
