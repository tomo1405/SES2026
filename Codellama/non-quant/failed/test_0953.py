import pytest
from src_0953 import task_func

def test_task_func_positive_n_tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 3
    employees = ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
    seed = 1234

    expected_assignment_data = [
        ["Task_1", "John Doe", "2023-02-28"],
        ["Task_2", "Jane Smith", "2023-02-28"],
        ["Task_3", "James Brown", "2023-02-28"]
    ]

    expected_assignment_df = pd.DataFrame(
        expected_assignment_data, columns=["Task Name", "Assigned To", "Due Date"]
    )

    assignment_df = task_func(task_list, n_tasks, employees, seed)

    assert assignment_df.equals(expected_assignment_df)

def test_task_func_negative_n_tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = -1
    employees = ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
    seed = 1234

    with pytest.raises(ValueError):
        task_func(task_list, n_tasks, employees, seed)