from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def task_func(L):
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    fig, ax = plt.subplots()
    ax.plot(standardized_data)
    plt.close(fig)
    return ax