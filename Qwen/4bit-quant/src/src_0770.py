from collections import Counter
import itertools
import operator
def task_func(list_of_menuitems):
    flat_list = list(itertools.chain(*list_of_menuitems))

    counter = Counter(flat_list)

    return max(counter.items(), key=operator.itemgetter(1))[0]