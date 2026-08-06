import numpy as np
from scipy.linalg import svd
def task_func(rows=3, columns=2, seed=0):
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    U, s, Vh = svd(matrix)

    return U, s, Vh