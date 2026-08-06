import pandas as pd
from random import uniform
def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):

    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=[column_name])

    return data_df