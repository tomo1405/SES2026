import heapq
import random
def task_func(k, list_length = 5, min_value = 0, max_value = 100):

    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    heapq.heapify(numbers)
    smallest_numbers = heapq.nsmallest(k, numbers)
   
    return numbers, smallest_numbers