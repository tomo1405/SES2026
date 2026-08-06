import numpy as np
import pandas as pd
# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(length, min_value = 0, max_value = 100):

    # Generate random data and create a DataFrame
    data = np.random.randint(min_value, max_value, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate the cumulative distribution function (CDF) for each column
    df = df.apply(lambda x: x.value_counts().sort_index().cumsum())

    return df