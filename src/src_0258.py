import numpy as np
import math
def task_func(ax, num_turns):

    r = np.linspace(0, num_turns * 2 * math.pi, 1000)
    theta = r

    ax.plot(theta, r)
    ax.set_rlabel_position(num_turns * 45)

    return ax