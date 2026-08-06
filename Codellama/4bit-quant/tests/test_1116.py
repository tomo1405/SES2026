from src_1116 import task_func


def test_task_func():
    dict1 = {'A': 2, 'B': 3, 'C': 1}
    employee_ids = task_func(dict1)
    assert len(employee_ids) == 6
    assert all(employee_id.startswith(prefix) for prefix, num_employees in dict1.items() for _ in range(num_employees))
    assert all(len(employee_id) == 5 for employee_id in employee_ids)
    assert all(employee_id.isalpha() for employee_id in employee_ids)