import pandas as pd
import numpy as np

def calculate_metrics(data, variable1, variable2):

    data = data.sort_values(by="time").reset_index(drop=True)

    
    data[f"High_Last_{variable1}_Days"] = data['high'].rolling(window=variable1, min_periods=1).max()
    data[f"Low_Last_{variable1}_Days"] = data['low'].rolling(window=variable1, min_periods=1).min()

    # Calculate the day since the last high and low
    data[f"Days_Since_High_Last_{variable1}_Days"] = (
        data['high'].rolling(window=variable1, min_periods=1).apply(lambda x: variable1 - np.argmax(x[::-1]) - 1)
    )
    data[f"Days_Since_Low_Last_{variable1}_Days"] = (
        data['low'].rolling(window=variable1, min_periods=1).apply(lambda x: variable1 - np.argmin(x[::-1]) - 1)
    )

    # Percentage difference from historical high and low
    data[f"%_Diff_From_High_Last_{variable1}_Days"] = (
        (data['close'] - data[f"High_Last_{variable1}_Days"]) / data[f"High_Last_{variable1}_Days"]
    ) * 100

    data[f"%_Diff_From_Low_Last_{variable1}_Days"] = (
        (data['close'] - data[f"Low_Last_{variable1}_Days"]) / data[f"Low_Last_{variable1}_Days"]
    ) * 100

    # Future Metrics
    data[f"High_Next_{variable2}_Days"] = data['high'].shift(-variable2).rolling(window=variable2, min_periods=1).max()
    data[f"Low_Next_{variable2}_Days"] = data['low'].shift(-variable2).rolling(window=variable2, min_periods=1).min()

    # Percentage difference from future high and low
    data[f"%_Diff_From_High_Next_{variable2}_Days"] = (
        (data['close'] - data[f"High_Next_{variable2}_Days"]) / data[f"High_Next_{variable2}_Days"]
    ) * 100

    data[f"%_Diff_From_Low_Next_{variable2}_Days"] = (
        (data['close'] - data[f"Low_Next_{variable2}_Days"]) / data[f"Low_Next_{variable2}_Days"]
    ) * 100

    return data
