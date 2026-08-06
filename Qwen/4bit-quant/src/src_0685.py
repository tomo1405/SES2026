import pandas as pd
import numpy as np
def task_func(df, col):
    # Remove specified column using pandas
    updated_df = pd.DataFrame(df).drop(col, axis=1)
    
    # Add a new column 'IsEvenIndex' using numpy to determine if index is even
    # The np.arange(len(updated_df)) creates an array of indexes, % 2 == 0 checks if they are even
    updated_df['IsEvenIndex'] = np.arange(len(updated_df)) % 2 == 0
    
    return updated_df