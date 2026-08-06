from sklearn.preprocessing import MinMaxScaler
import numpy as np
def task_func(myList):
    myList = np.array(myList).reshape(-1, 1)
    scaler = MinMaxScaler()
    normalized_list = scaler.fit_transform(myList)

    return normalized_list.flatten()