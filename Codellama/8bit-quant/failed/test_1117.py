import pytest
from src_1117 import task_func

def test_task_func():
    # Test case 1: No employees in EMP$$ department
    dict1 = {'EMP$$': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

    # Test case 2: One employee in EMP$$ department
    dict1 = {'EMP$$': 1}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 3: Multiple employees in EMP$$ department
    dict1 = {'EMP$$': 5}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 38
    assert median_age == 38
    assert mode_age == [38]

    # Test case 4: Multiple employees in EMP$$ department with different ages
    dict1 = {'EMP$$': 5, 'EMP$$2': 3}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 38
    assert median_age == 38
    assert mode_age == [38]

    # Test case 5: No employees in EMP$$ department with other departments
    dict1 = {'EMP$$': 0, 'EMP$$2': 3}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []