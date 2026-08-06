import collections
import pandas as pd
def task_func(obj_list, attr):
    attr_values = [getattr(obj, attr) for obj in obj_list]
    count = collections.Counter(attr_values)
    if len(count.keys()) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(count, orient='index').reset_index()
    df = df.rename(columns={'index':'attribute', 0:'count'})
    return df