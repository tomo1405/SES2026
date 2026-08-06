import pytest
from src_1090 import task_func

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]

def test_task_func():
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 15
    assert category_counts == {'a': 2, 'b': 2, 'c': 1}

if __name__ == "__main__":
    pytest.main()