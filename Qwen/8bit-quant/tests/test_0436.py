import pytest
from src_0436 import task_func
import pandas as pd

def test_task_func_valid_employee():
    name = "John"
    age = 30
    code = "E123"
    salary = 75000.0
    bio = "Experienced software developer"
    
    df = task_func(name, age, code, salary, bio)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 6)
    assert df.iloc[0]['Name'] == name
    assert df.iloc[0]['Age'] == age
    assert df.iloc[0]['Code'] == code
    assert df.iloc[0]['Salary'] == salary
    assert df.iloc[0]['Bio'] == bio
    assert df.iloc[0]['Job Title'] in ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

def test_task_func_invalid_employee():
    with pytest.raises(ValueError):
        task_func("Jane", 25, "E456", 60000.0, "Junior developer")

def test_task_func_invalid_age():
    with pytest.raises(TypeError):
        task_func("John", "thirty", "E123", 75000.0, "Experienced software developer")

def test_task_func_invalid_salary():
    with pytest.raises(TypeError):
        task_func("John", 30, "E123", "seventy five thousand", "Experienced software developer")