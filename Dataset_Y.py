import pandas as pd
import numpy as np


data = {
    'Feature5': df_with_metrics['%_Diff_From_High_Next_5_Days'].to_numpy(),
    'Feature6': df_with_metrics['%_Diff_From_Low_Next_5_Days'].to_numpy()
}

df_new_y = pd.DataFrame(data)


Y = df_new_y.to_numpy()  

Y = df_new_y.values 

print("Features Array:")
print(Y)
