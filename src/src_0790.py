import numpy as np
from sklearn.preprocessing import MinMaxScaler
# Constants
ARRAY_LENGTH = 10
def task_func():
    np.random.seed(42)  # For reproducibility, as shown in your example
    array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array)
    return scaled_array