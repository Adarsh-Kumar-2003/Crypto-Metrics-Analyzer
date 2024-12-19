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

def get_crypto_data(df, target_date):

    # Convert target_date to datetime format for matching
    target_date = pd.to_datetime(target_date)

   
    result = df[df['time'] == target_date]

    if not result.empty:
        return {
            'Date': result['time'].iloc[0],
            'Open': result['open'].iloc[0],
            'High': result['high'].iloc[0],
            'Low': result['low'].iloc[0],
            'Close': result['close'].iloc[0],
        }
    else:
        return f"No data found for the date: {target_date.strftime('%Y-%m-%d')}"
