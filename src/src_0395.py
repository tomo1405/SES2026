import collections
import string
import random
def task_func(length, seed=0):
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    char_freq = collections.Counter(random_string)

    return dict(char_freq)