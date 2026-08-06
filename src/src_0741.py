from collections import Counter
import heapq
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(my_dict):
    letter_counter = Counter(my_dict)
    most_common_letters = heapq.nlargest(3, letter_counter, key=letter_counter.get)

    return most_common_letters