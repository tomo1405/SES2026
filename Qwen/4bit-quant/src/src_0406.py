import random
import matplotlib.pyplot as plt
def task_func(points: int):
    x = list(range(points))
    y = [random.random() for _ in range(points)]

    _, ax = plt.subplots()
    ax.plot(x, y)

    return y, ax