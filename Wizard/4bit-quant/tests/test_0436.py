python
import pandas as pd
import random
from src_0436 import task_func

def test_task_func():
    # Test valid input
    valid_input = {
        "name": "John",
        "age": 30,
        "code": "1234",
        "salary": 50000.0,
        "bio": "I am a software engineer.",
    }
    expected_output = pd.DataFrame(
        [
            ["John", 30, "1234", 50000.0, "I am a software engineer.", "Engineer"]
        ],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    assert task_func(**valid_input).equals(expected_output)

    # Test invalid name input
    invalid_name_input = {
        "name": "Jane",
        "age": 30,
        "code": "1234",
        "salary": 50000.0,
        "bio": "I am a software engineer.",
    }
    with pytest.raises(ValueError):
        task_func(**invalid_name_input)

    # Test invalid age input
    invalid_age_input = {
        "name": "John",
        "age": "30",
        "code": "1234",
        "salary": 50000.0,
        "bio": "I am a software engineer.",
    }
    with pytest.raises(TypeError):
        task_func(**invalid_age_input)

    # Test invalid code input
    invalid_code_input = {
        "name": "John",
        "age": 30,
        "code": 1234,
        "salary": 50000.0,
        "bio": "I am a software engineer.",
    }
    with pytest.raises(TypeError):
        task_func(**invalid_code_input)

    # Test invalid salary input
    invalid_salary_input = {
        "name": "John",
        "age": 30,
        "code": "1234",
        "salary": "50000.0",
        "bio": "I am a software engineer.",
    }
    with pytest.raises(TypeError):
        task_func(**invalid_salary_input)

    # Test invalid bio input
    invalid_bio_input = {
        "name": "John",
        "age": 30,
        "code": "1234",
        "salary": 50000.0,
        "bio": 1234,
    }
    with pytest.raises(TypeError):
        task_func(**invalid_bio_input)