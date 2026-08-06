import pytest
from src_0953 import task_func

def test_task_func_with_valid_inputs():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 3
    employees = ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
    seed = 1234

    expected_output = pd.DataFrame(
        [
            ["Task_1", "John Doe", "2023-02-28"],
            ["Task_2", "Jane Smith", "2023-02-28"],
            ["Task_3", "James Brown", "2023-02-28"],
        ],
        columns=["Task Name", "Assigned To", "Due Date"],
    )

    output = task_func(task_list, n_tasks, employees, seed)

    assert output.equals(expected_output)

def test_task_func_with_invalid_inputs():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = -1
    employees = ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
    seed = 1234

    with pytest.raises(ValueError):
        task_func(task_list, n_tasks, employees, seed)