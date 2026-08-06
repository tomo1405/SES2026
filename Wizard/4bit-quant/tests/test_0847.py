python
import collections
import pandas as pd
from src_0847 import task_func

def test_task_func():
    obj_list = [
        {'name': 'John', 'age': 25, 'gender': 'male'},
        {'name': 'Jane', 'age': 30, 'gender': 'female'},
        {'name': 'Bob', 'age': 20, 'gender': 'male'},
        {'name': 'Alice', 'age': 35, 'gender': 'female'},
        {'name': 'Tom', 'age': 40, 'gender': 'male'},
        {'name': 'Mary', 'age': 28, 'gender': 'female'},
    ]

    attr = 'age'
    expected_df = pd.DataFrame({
        'attribute': [20, 25, 30, 35, 40],
        'count': [1, 1, 1, 1, 1]
    })

    result_df = task_func(obj_list, attr)

    assert result_df.equals(expected_df)