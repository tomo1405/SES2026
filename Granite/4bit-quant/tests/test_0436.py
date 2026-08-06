import pandas as pd
from random import randint
from src_0436 import task_func
import pytest

def test_task_func():
    name = "John"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "Experienced engineer with 5 years of experience."
    expected_output = pd.DataFrame(
        [[name, age, code, salary, bio, "Engineer"]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    actual_output = task_func(name, age, code, salary, bio)
    assert actual_output.equals(expected_output)

def test_task_func_invalid_name():
    name = "Eva"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "Experienced engineer with 5 years of experience."
    with pytest.raises(ValueError) as exc_info:
        task_func(name, age, code, salary, bio)
    assert "Invalid employee name. Must be one of" in str(exc_info.value)