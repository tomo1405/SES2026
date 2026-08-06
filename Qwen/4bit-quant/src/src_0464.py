import numpy as np
import pandas as pd
def task_func(data_str, separator=",", bins=20):

    data = np.fromstring(data_str, sep=separator)
    if data.size == 0:
        raise ValueError("Failed to find valid data")

    data = pd.Series(data, dtype='int64')
    ax = data.plot.hist(grid=True, bins=bins, rwidth=0.9, color="#607c8e")
    return data, ax