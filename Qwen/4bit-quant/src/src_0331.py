import heapq
import random
def task_func(list_length:5, k:int):

    
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
   
    return numbers, largest_numbers