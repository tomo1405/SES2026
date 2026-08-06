import pytest
from src_0436 import task_func
import pandas as pd

def test_task_func_valid_name():
    name = "John"
    age = 30
    code = "E123"
    salary = 75000.0
    bio = "Experienced software developer"
    
    df = task_func(name, age, code, salary, bio)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 6)
    assert df.iloc[0]["Name"] == name
    assert df.iloc[0]["Age"] == age
    assert df.iloc[0]["Code"] == code
    assert df.iloc[0]["Salary"] == salary
    assert df.iloc[0]["Bio"] == bio
    assert df.iloc[0]["Job Title"] in ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

def test_task_func_invalid_name():
    name = "Eve"
    age = 28
    code = "E456"
    salary = 60000.0
    bio = "Junior software developer"
    
    with pytest.raises(ValueError) as exc_info:
        task_func(name, age, code, salary, bio)
    assert str(exc_info.value) == "Invalid employee name. Must be one of ['John', 'Alice', 'Bob', 'Charlie', 'David']"

def test_task_func_random_job_assignment():
    name = "Alice"
    age = 35
    code = "E789"
    salary = 80000.0
    bio = "Team lead"
    
    df = task_func(name, age, code, salary, bio)
    assert df.iloc[0]["Job Title"] in ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

def test_task_func_data_types():
    name = "Bob"
    age = 40
    code = "E012"
    salary = 90000.0
    bio = "Senior software developer"
    
    df = task_func(name, age, code, salary, bio)
    assert isinstance(df.iloc[0]["Name"], str)
    assert isinstance(df.iloc[0]["Age"], int)
    assert isinstance(df.iloc[0]["Code"], str)
    assert isinstance(df.iloc[0]["Salary"], float)
    assert isinstance(df.iloc[0]["Bio"], str)
    assert isinstance(df.iloc[0]["Job Title"], str)