import seaborn as sns
from src_0417 import task_func


def test_task_func_with_default_column():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    }
    result = task_func(data)
    assert isinstance(result, sns.axisgrid.FacetGrid)

def test_task_func_with_non_default_column():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'd': [7, 8, 9]
    }
    result = task_func(data, column='d')
    assert isinstance(result, sns.axisgrid.FacetGrid)

def test_task_func_with_no_numeric_columns():
    data = {
        'a': ['x', 'y', 'z'],
        'b': ['p', 'q', 'r']
    }
    result = task_func(data)
    assert result is None

def test_task_func_with_empty_data():
    data = {}
    result = task_func(data)
    assert result is None

def test_task_func_with_all_numeric_columns():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    }
    result = task_func(data, column='a')
    assert isinstance(result, sns.axisgrid.FacetGrid)

def test_task_func_with_one_numeric_column():
    data = {
        'a': [1, 2, 3],
        'b': ['p', 'q', 'r']
    }
    result = task_func(data)
    assert isinstance(result, sns.axisgrid.FacetGrid)