import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(rows=3, columns=2, seed=42):
    np.random.seed(seed) # Ensure reproducibility for consistent outputs across different runs
    matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    return scaled_matrix