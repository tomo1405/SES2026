import numpy as np
import random
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    if l is None:
        l = ELEMENTS.copy()  # Use a copy to avoid modifying the original list
    random.shuffle(l)
    arr = np.array(l)
    arr = np.concatenate((arr[3:], arr[:3]))
    return arr