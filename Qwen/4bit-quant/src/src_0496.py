import pandas as pd
import numpy as np
def task_func(days, random_seed=0):
    np.random.seed(random_seed)
    date_rng = pd.date_range(start="2023-01-01", periods=days, freq="D")
    df = pd.DataFrame(date_rng, columns=["date"])
    df.set_index("date", inplace=True)
    categories = ["Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    for category in categories:
        df[category] = np.random.randint(0, 100, size=(days))

    return df