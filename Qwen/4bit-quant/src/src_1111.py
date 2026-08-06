from collections import Counter
from operator import itemgetter
import itertools
def task_func(word_dict):
    letters = list(itertools.chain.from_iterable(word_dict.keys()))
    count_dict = dict(Counter(letters))
    
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    
    return sorted_dict