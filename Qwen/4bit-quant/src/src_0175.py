import pandas as pd
import numpy as np
def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    
    random_generated = np.random.randint(min_value, max_value + 1, size=len(data))
    data[key] = random_generated
    return data