import pytest
from src_0523 import task_func

def test_task_func_empty_data():
    data = []
    ax = task_func(data)
    assert ax is None

def test_task_func_invalid_data():
    data = [{"name": "John", "score": -1}]
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_valid_data():
    data = [{"name": "John", "score": 80}, {"name": "Jane", "score": 90}]
    ax = task_func(data)
    assert ax is not None
    assert ax.get_title() == "Average Student Scores"
    assert ax.get_xlabel() == "Student"
    assert ax.get_ylabel() == "Average Score"
    assert len(ax.get_xticklabels()) == 2
    assert len(ax.get_yticklabels()) == 2
    assert ax.get_xticklabels()[0].get_text() == "John"
    assert ax.get_xticklabels()[1].get_text() == "Jane"
    assert ax.get_yticklabels()[0].get_text() == "80"
    assert ax.get_yticklabels()[1].get_text() == "90"