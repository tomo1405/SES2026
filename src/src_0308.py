import seaborn as sns
import matplotlib.pyplot as plt
import random
def task_func(list_of_lists, seed=0):
    random.seed(seed)
    data = []
    # Initialize a fresh plot
    plt.figure()
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(5)]

    plot = sns.histplot(data)
    return plot