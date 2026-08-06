import random
import matplotlib.pyplot as plt
# Sample data
class Object:
    value = 0
    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value
def task_func(obj_list, attr, num_bins=30, seed=0):
    # Set random seed
    random.seed(seed)
    attr_values = [getattr(obj, attr) for obj in obj_list]

    # Generate histogram
    fig, ax = plt.subplots()
    ax.hist(attr_values, bins=num_bins, alpha=0.5)
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')

    return ax