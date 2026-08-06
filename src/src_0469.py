import pandas as pd
import numpy as np
def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    df = pd.read_csv(file_path, dtype=float)
    ax = df[columns].plot()
    croot = np.cbrt(df[columns])
    return df, ax, croot