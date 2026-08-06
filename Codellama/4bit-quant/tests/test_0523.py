import pytest
from src_0523 import task_func

def test_task_func():
    data = [{"student1": 10, "student2": 20, "student3": 30},
            {"student1": 15, "student2": 25, "student3": 35},
            {"student1": 20, "student2": 30, "student3": 40}]
    ax = task_func(data)
    assert ax is not None
    assert ax.get_title() == "Average Student Scores"
    assert ax.get_xlabel() == "Student"
    assert ax.get_ylabel() == "Average Score"
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticks()[0] == "student1"
    assert ax.get_xticks()[1] == "student2"
    assert ax.get_xticks()[2] == "student3"
    assert ax.get_yticks()[0] == 10
    assert ax.get_yticks()[1] == 20
    assert ax.get_yticks()[2] == 30
    assert ax.get_yticks()[3] == 15
    assert ax.get_yticks()[4] == 25
    assert ax.get_yticks()[5] == 35
    assert ax.get_yticks()[6] == 20
    assert ax.get_yticks()[7] == 30
    assert ax.get_yticks()[8] == 40

def test_task_func_empty_data():
    data = []
    ax = task_func(data)
    assert ax is None

def test_task_func_negative_scores():
    data = [{"student1": -10, "student2": 20, "student3": 30}]
    with pytest.raises(ValueError):
        task_func(data)