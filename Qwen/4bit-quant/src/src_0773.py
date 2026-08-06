import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
def task_func(num_samples=1000, k=5, d=2,  random_seed=None):

    if random_seed is not None:
        np.random.seed(random_seed)
    data = np.random.randn(num_samples, 1)*k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    mse = mean_squared_error(data, scaled_data)

    return mse