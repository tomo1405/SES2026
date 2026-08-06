import pytest
from src_0118 import task_func

def test_task_func_num_of_students():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_default_parameters():
    df = task_func(5)
    assert len(df) == 5
    assert all(df['Name'].isin(['John', 'Mike', 'Sara', 'Emma', 'Nick']))
    assert all(df['Gender'].isin(['Male', 'Female']))
    assert all(df['Age'].between(15, 20))
    assert all(df['Score'].between(50, 100))

def test_task_func_custom_name_list():
    df = task_func(5, name_list=['Alice', 'Bob'])
    assert all(df['Name'].isin(['Alice', 'Bob']))

def test_task_func_custom_gender_list():
    df = task_func(5, gender_list=['Other'])
    assert all(df['Gender'] == 'Other')

def test_task_func_custom_age_range():
    df = task_func(5, age_range=(10, 30))
    assert all(df['Age'].between(10, 30))

def test_task_func_custom_score_range():
    df = task_func(5, score_range=(70, 90))
    assert all(df['Score'].between(70, 90))

def test_task_func_reproducibility():
    df1 = task_func(5, seed=42)
    df2 = task_func(5, seed=42)
    assert df1.equals(df2)