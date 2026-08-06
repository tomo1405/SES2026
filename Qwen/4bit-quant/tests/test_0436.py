import pandas as pd
import pytest
from src_0436 import task_func


def test_task_func_valid_name():
    name = "Alice"
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
    with pytest.raises(ValueError):
        task_func("Eve", 28, "E456", 80000.0, "Data scientist")

def test_task_func_min_age():
    name = "Bob"
    age = 18
    code = "E789"
    salary = 50000.0
    bio = "Entry-level programmer"
    
    df = task_func(name, age, code, salary, bio)
    
    assert df.iloc[0]["Age"] == age

def test_task_func_max_salary():
    name = "Charlie"
    age = 45
    code = "E101"
    salary = 150000.0
    bio = "Senior software architect"
    
    df = task_func(name, age, code, salary, bio)
    
    assert df.iloc[0]["Salary"] == salary

def test_task_func_empty_bio():
    name = "David"
    age = 35
    code = "E102"
    salary = 90000.0
    bio = ""
    
    df = task_func(name, age, code, salary, bio)
    
    assert df.iloc[0]["Bio"] == bio