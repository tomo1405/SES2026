import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0
def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    if max_value < min_value:
        raise ValueError()

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    return pd.DataFrame(normalized_data, columns=['Normalized Value'])