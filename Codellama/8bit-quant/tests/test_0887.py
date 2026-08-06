import pytest
from src_0887 import task_func

def test_task_func():
    data = {'Name': 'John', 'Age': 25, 'Score': 90}
    df, avg_scores, most_common_age = task_func(data)
    assert df.equals(pd.DataFrame({'Name': 'John', 'Age': 25, 'Score': 90}))
    assert avg_scores == 90
    assert most_common_age == 25

def test_task_func_missing_key():
    data = {'Name': 'John', 'Age': 25}
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_invalid_key():
    data = {'Name': 'John', 'Age': 25, 'Score': 'A'}
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_invalid_data_type():
    data = {'Name': 'John', 'Age': 25, 'Score': 90}
    with pytest.raises(TypeError):
        task_func(data, data_type='invalid')

def test_task_func_invalid_sort_by():
    data = {'Name': 'John', 'Age': 25, 'Score': 90}
    with pytest.raises(ValueError):
        task_func(data, sort_by='invalid')

def test_task_func_invalid_groupby():
    data = {'Name': 'John', 'Age': 25, 'Score': 90}
    with pytest.raises(ValueError):
        task_func(data, groupby='invalid')