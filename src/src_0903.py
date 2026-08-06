import pandas as pd
from collections import Counter
def task_func(d):
    df = pd.DataFrame(d)
    counts = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            counts[key] = Counter(df[key].dropna().tolist())
        else:
            counts[key] = Counter()

    return counts