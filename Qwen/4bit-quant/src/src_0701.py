import pandas as pd
import numpy as np
def task_func(data, cols):
    df = pd.DataFrame(data, columns=cols)
    
    df_np = np.array(df)
    df = pd.DataFrame(df_np, columns=cols)
    
    correlation_matrix = df.corr()
    return correlation_matrix