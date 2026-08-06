import numpy as np
from scipy import stats
def task_func(df):

    p_values = {}

    for col in df.columns:
        column_data = np.array(df[col])
        
        test_stat, p_value = stats.shapiro(column_data)
        
        p_values[col] = p_value

    return p_values