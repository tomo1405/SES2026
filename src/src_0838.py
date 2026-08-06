import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    
    for i in scale_cols:
        scaler = StandardScaler()
        df[columns[i]] = scaler.fit_transform(df[[columns[i]]])
    
    return df