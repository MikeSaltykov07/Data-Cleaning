import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%%
def clean_type_data(data: pd.DataFrame):
  data = data.fillna(0)
  data_columns = [_ for _ in data.columns if _ not in ['Timestamp', 'Timestamp15_15', 'Timestamp_15'] ]
  
  for column in data_columns:
    if isinstance(data.loc[1, column],  np.int64):
        maxVal = data[column].max()
        if maxVal < 120:
            data[column] = data[column].astype(np.int8)
        elif maxVal < 32767:
            data[column] = data[column].astype(np.int16)
        else:
            data[column] = data[column].astype(np.int32)     
    if isinstance(data.loc[1, column], np.float64):

        maxVal = data[column].max()
        if maxVal < 120:
            data[column] = data[column].astype(np.float16)
        else:
            data[column] = data[column].astype(np.float32)
  return data