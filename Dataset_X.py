import pandas as pd
import numpy as np


data = {
    'Feature1': df_with_metrics['Days_Since_High_Last_7_Days'].to_numpy(),
    'Feature2': df_with_metrics['Days_Since_Low_Last_7_Days'].to_numpy(),
    'Feature3': df_with_metrics['%_Diff_From_High_Last_7_Days'].to_numpy(),
    'Feature4': df_with_metrics['%_Diff_From_Low_Last_7_Days'].to_numpy()
}

df_new_w = pd.DataFrame(data)


X = df_new_w.to_numpy()  

X = df_new_w.values 



#print("Features Array:")
#print(X)
