import pytest
from src_0092 import task_func

def test_task_func():
    data = ... # provide test data
    column1 = ... # provide test column1
    column2 = ... # provide test column2
    expected_output = ... # provide expected output

    with pytest.raises(ValueError):
        # Test if ValueError is raised when specified columns do not exist in the DataFrame
        task_func(data, "nonexistent_column1", "nonexistent_column2")

    output, ax = task_func(data, column1, column2)

    assert output == expected_output # Test if the output matches the expected output

    # Test if the plot is created correctly
    assert ax.get_legend() is not None
    assert ax.get_lines() is not None