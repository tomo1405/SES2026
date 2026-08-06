import numpy as np
import pandas as pd
def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    np.random.seed(seed)
    columns = sorted(list(set(columns)))
    data = np.random.rand(rows, len(columns))
    np.random.shuffle(columns)
    df = pd.DataFrame(data, columns=columns)
    return df