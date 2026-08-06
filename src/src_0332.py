import bisect
import random
def task_func(num, list_length = 5, min_value = 0, max_value = 0):

    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    sorted_list = numbers.copy()
    bisect.insort(sorted_list, num)
    return numbers, sorted_list