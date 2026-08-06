import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data, columns=columns)

    if fill_missing:
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)

    return df