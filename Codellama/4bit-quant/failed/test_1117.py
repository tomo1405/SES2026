import pytest
from src_1117 import task_func

def test_task_func():
    # Test case 1: No employees in EMP$$ department
    dict1 = {'EMP$$1': 0, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

    # Test case 2: One employee in EMP$$ department
    dict1 = {'EMP$$1': 1, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 3: Multiple employees in EMP$$ department
    dict1 = {'EMP$$1': 3, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 4: No employees in EMP$$ department
    dict1 = {'EMP$$1': 0, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

    # Test case 5: One employee in EMP$$ department
    dict1 = {'EMP$$1': 1, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 6: Multiple employees in EMP$$ department
    dict1 = {'EMP$$1': 3, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 7: No employees in EMP$$ department
    dict1 = {'EMP$$1': 0, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

    # Test case 8: One employee in EMP$$ department
    dict1 = {'EMP$$1': 1, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 9: Multiple employees in EMP$$ department
    dict1 = {'EMP$$1': 3, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 22
    assert median_age == 22
    assert mode_age == [22]

    # Test case 10: No employees in EMP$$ department
    dict1 = {'EMP$$1': 0, 'EMP$$2': 0}
    mean_age, median_age, mode_age = task_func(dict1)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []