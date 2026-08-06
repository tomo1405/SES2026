import pandas as pd
from random import randint
from src_0436 import task_func
import pytest

def test_task_func():
    name = "John"
    age = 30
    code = "ABC123"
    salary = 50000.0
    bio = "Engineer at XYZ Company"
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
    bio = "Engineer at ABC Company"
    with pytest.raises(ValueError) as excinfo:
        task_func(name, age, code, salary, bio)
    assert "Invalid employee name. Must be one of" in str(excinfo.value)