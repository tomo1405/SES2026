import pytest
from src_0870 import task_func

def test_task_func():
    # Test 1: Test with default values
    expected_output = pd.DataFrame([['Alice', 1], ['Bob', 2], ['Charlie', 3], ['David', 4], ['Eve', 5]], columns=['Student', 'Grade'])
    assert task_func(5).equals(expected_output)

    # Test 2: Test with custom values
    expected_output = pd.DataFrame([['Alice', 1], ['Bob', 2], ['Charlie', 3], ['David', 4], ['Eve', 5]], columns=['Student', 'Grade'])
    assert task_func(5, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'], grade_range=range(1, 6)).equals(expected_output)

    # Test 3: Test with invalid values
    with pytest.raises(ValueError):
        task_func(0)

    with pytest.raises(ValueError):
        task_func(5, students=[])

    with pytest.raises(ValueError):
        task_func(5, grade_range=[])