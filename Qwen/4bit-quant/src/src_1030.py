import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    column_names = [
        chr(97 + i) for i in range(columns)
    ]  # generate column names based on the number of columns
    values = list("abcdefghijklmnopqrstuvwxyz")
    data = np.random.choice(values, size=(rows, columns))
    df = pd.DataFrame(data, columns=column_names)
    return df