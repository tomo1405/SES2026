import numpy as np
from scipy.stats import mode
def task_func(list_of_lists):
    merged_list = np.array([item for sublist in list_of_lists for item in sublist])
    mode_value, mode_count = mode(merged_list)
    return mode_value, mode_count