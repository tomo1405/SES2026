import pandas as pd
from statistics import mean
def task_func(df: pd.DataFrame) -> dict:

    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError('The DataFram should have the columns "Name" and "Score".')

    grouped = df.groupby('Name')
    result_dict = {}
    for name, group in grouped:
        avg_score = mean(group['Score'])
        result_dict[name] = iter([(name, avg_score)])

    return result_dict