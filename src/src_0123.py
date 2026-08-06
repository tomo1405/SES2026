import numpy as np
import random
def task_func(my_list):
    random_number = random.randint(0, 100)
    my_list.append(random_number)

    size = sum(my_list)
    random_array = np.random.rand(size)

    return random_array