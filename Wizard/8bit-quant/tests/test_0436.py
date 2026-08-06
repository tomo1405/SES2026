python
import pandas as pd
import random
from src_0436 import task_func

def test_task_func():
    name = "John"
    age = 30
    code = "12345"
    salary = 50000.0
    bio = "I am a Python testing engineer."

    data_df = task_func(name, age, code, salary, bio)

    assert isinstance(data_df, pd.DataFrame)
    assert data_df.shape == (1, 6)
    assert data_df.columns.tolist() == ["Name", "Age", "Code", "Salary", "Bio", "Job Title"]
    assert data_df.loc[0, "Name"] == name
    assert data_df.loc[0, "Age"] == age
    assert data_df.loc[0, "Code"] == code
    assert data_df.loc[0, "Salary"] == salary
    assert data_df.loc[0, "Bio"] == bio
    assert data_df.loc[0, "Job Title"] in ["Engineer", "Manager", "Analyst", "Developer", "Tester"]