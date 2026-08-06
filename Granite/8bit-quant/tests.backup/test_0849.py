import heapq
import random
from src_0849 import task_func

def test_task_func():
    obj_list = [1, 2, 3, 4, 5]
    attr = 'value'
    top_n = 3
    seed = 123

    random.seed(seed)
    random_value = random.choice([1, 2, 3, 4, 5])

    top_values = heapq.nlargest(top_n, [1, 2, 3, 4, 5])

    assert task_func(obj_list, attr, top_n, seed)[0] == top_values
    assert task_func(obj_list, attr, top_n, seed)[1] == random_value

def test_task_func_with_empty_list():
    obj_list = []
    attr = 'value'
    top_n = 3
    seed = 123

    random.seed(seed)
    random_value = random.choice([])

    top_values = heapq.nlargest(top_n, [])

    assert task_func(obj_list, attr, top_n, seed)[0] == top_values
    assert task_func(obj_list, attr, top_n, seed)[1] == random_value