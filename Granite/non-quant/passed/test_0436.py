import pandas as pd
from random import randint
from src_0436 import task_func
import pytest

def test_task_func():
    name = "Alice"
    age = 30
    code = "ABC123"
    salary = 60000.0
    bio = "Alice is a software engineer with 5 years of experience."
    expected_df = pd.DataFrame(
        [[name, age, code, salary, bio, "Engineer"]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    actual_df = task_func(name, age, code, salary, bio)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_name():
    name = "Eve"
    age = 30
    code = "XYZ789"
    salary = 60000.0
    bio = "Eve is a software engineer with 5 years of experience."
    with pytest.raises(ValueError) as exc_info:
        task_func(name, age, code, salary, bio)
    assert "Invalid employee name. Must be one of" in str(exc_info.value)