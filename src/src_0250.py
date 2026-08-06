import pandas as pd
import random
from sklearn.model_selection import train_test_split
def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    train_data, test_data = train_test_split(data_df, test_size=test_size)

    return train_data, test_data