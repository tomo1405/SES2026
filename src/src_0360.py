from scipy import stats
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    x = data_dict[data_keys[0]]
    y = data_dict[data_keys[1]]
    correlation, _ = stats.pearsonr(x, y)
    
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    return correlation, ax