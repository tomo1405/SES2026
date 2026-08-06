from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    array1 = np.array([randint(1, 100) for _ in range(array_length)])
    array2 = np.array([randint(1, 100) for _ in range(array_length)])

    max_values = np.maximum(array1, array2)

    fig, ax = plt.subplots()
    ax.plot(max_values)
    ax.set_ylabel('Maximum Values')
    
    return ax