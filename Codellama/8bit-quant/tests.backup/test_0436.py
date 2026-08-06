import pytest
from src_0436 import task_func

def test_task_func_valid_input():
    name = "John"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "I am a software engineer."
    expected_df = pd.DataFrame(
        [[name, age, code, salary, bio, "Engineer"]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    assert task_func(name, age, code, salary, bio).equals(expected_df)

def test_task_func_invalid_name():
    name = "Jim"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "I am a software engineer."
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)

def test_task_func_invalid_age():
    name = "John"
    age = -1
    code = "12345"
    salary = 50000.0
    bio = "I am a software engineer."
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)

def test_task_func_invalid_code():
    name = "John"
    age = 30
    code = "1234"
    salary = 50000.0
    bio = "I am a software engineer."
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)

def test_task_func_invalid_salary():
    name = "John"
    age = 30
    code = "12345"
    salary = -1.0
    bio = "I am a software engineer."
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)

def test_task_func_invalid_bio():
    name = "John"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "I am a software engineer." * 100
    with pytest.raises(ValueError):
        task_func(name, age, code, salary, bio)