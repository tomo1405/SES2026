import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(my_dict):
    if not isinstance(my_dict["array"], np.ndarray):
        raise TypeError

    SCALER = MinMaxScaler()
    array = my_dict['array'].reshape(-1, 1)
    normalized_array = SCALER.fit_transform(array).reshape(-1)

    my_dict['normalized_array'] = normalized_array

    return my_dict