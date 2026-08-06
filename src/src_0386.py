import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    fruit_list = [item for item in fruit_dict.values() if isinstance(item, str) and item in FRUITS]
    fruit_counter = Counter(fruit_list)
    
    plt.bar(fruit_counter.keys(), fruit_counter.values())
    return Counter([item for item in fruit_dict.values() if isinstance(item, str)]), plt.gca()