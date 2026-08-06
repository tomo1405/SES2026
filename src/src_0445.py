import numpy as np
import matplotlib.pyplot as plt
def task_func(n_points=100, random_seed=None):
    np.random.seed(random_seed)
    points = np.random.random((n_points, 3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])

    return points, ax