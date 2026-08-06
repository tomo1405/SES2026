import pandas as pd
import pytest
from src_0436 import task_func


def test_task_func():
    # Test with valid inputs
    name = "John"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "I am a software engineer."
    data_df = task_func(name, age, code, salary, bio)
    assert data_df.equals(pd.DataFrame(
        [[name, age, code, salary, bio, "Engineer"]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    ))

    # Test with invalid inputs
    name = "Jane"
    age = 25
    code = "67890"
    salary = 40000.0
    bio = "I am a data analyst."
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)