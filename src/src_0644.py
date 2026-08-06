import re
import pandas as pd
import numpy as np
# Constants
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    for col in dataframe.columns:
        dataframe[col] = dataframe[col].apply(lambda x: float(re.search(data_pattern, x).group(0)[1:-1])
                                              if pd.notnull(x) and re.search(data_pattern, x) else np.nan)
    return dataframe