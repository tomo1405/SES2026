import collections
import random
# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def task_func(n_keys, n_values):

    keys = [random.choice(LETTERS) for _ in range(n_keys)]
    values = list(range(1, n_values + 1))
    return dict(collections.OrderedDict((k, values) for k in keys))