import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    
    return ax