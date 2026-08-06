import pandas as pd
import numpy as np
# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']
def task_func(df, dct):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    # Replace values using dictionary mapping
    df = df.replace(dct)
    
    # Calculate the correlation matrix
    correlation_matrix = np.corrcoef(df.values, rowvar=False)
    
    return pd.DataFrame(correlation_matrix, columns=df.columns, index=df.columns)