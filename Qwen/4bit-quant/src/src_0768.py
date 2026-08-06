from collections import Counter
import random
import string
# Constants
LETTERS = string.ascii_letters
def task_func(list_of_lists):
    flat_list = [random.choice(LETTERS) for _ in list_of_lists]

    return dict(Counter(flat_list))