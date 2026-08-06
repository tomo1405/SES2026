from collections import Counter
import random
import itertools
def task_func(length, count, seed=0):
    random.seed(seed)
    strings = [''.join(random.choices(['a', 'b', 'c', 'd', 'e'], k=length)) for _ in range(count)]
    letter_frequency = Counter(itertools.chain(*strings))
    
    return letter_frequency