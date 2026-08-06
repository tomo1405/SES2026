python
import pandas as pd
from random import randint
import pytest

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "David"]
    JOBS = ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

    if name not in EMPLOYEES:
        raise ValueError(f"Invalid employee name. Must be one of {EMPLOYEES}")

    job = JOBS[randint(0, len(JOBS) - 1)]
    data_df = pd.DataFrame(
        [[name, age, code, salary, bio, job]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    return data_df

def test_task_func():
    # Test valid input
    valid_input = {
        "name": "John",
        "age": 30,
        "code": "12345",
        "salary": 50000.0,
        "bio": "I am a software engineer.",
    }
    expected_output = pd.DataFrame(
        [["John", 30, "12345", 50000.0, "I am a software engineer.", "Engineer"]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    assert task_func(**valid_input).equals(expected_output)

    # Test invalid input
    invalid_input = {
        "name": "Jane",
        "age": 25,
        "code": "67890",
        "salary": 60000.0,
        "bio": "I am a data analyst.",
    }
    with pytest.raises(ValueError):
        task_func(**invalid_input)