import string
import random
def task_func(length, random_seed=None):
    random.seed(random_seed)
    # Constants
    BRACKETS = "(){}[]"
    return ''.join(random.choice(string.ascii_lowercase + BRACKETS) for _ in range(length))