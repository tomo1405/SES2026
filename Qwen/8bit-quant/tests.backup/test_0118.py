import pytest
from src_0118 import task_func

def test_task_func_zero_students():
    with pytest.raises(ValueError) as excinfo:
        task_func(0)
    assert str(excinfo.value) == "num_of_students must be positive."

def test_task_func_negative_students():
    with pytest.raises(ValueError) as excinfo:
        task_func(-1)
    assert str(excinfo.value) == "num_of_students must be positive."

def test_task_func_default_parameters():
    df = task_func(3)
    assert len(df) == 3
    assert list(df.columns) == ['Name', 'Age', 'Gender', 'Score']
    assert all(df['Age'].between(15, 20))
    assert all(df['Score'].between(50, 100))

def test_task_func_custom_name_and_gender_lists():
    df = task_func(3, name_list=['Alice', 'Bob'], gender_list=['Other'])
    assert all(df['Name'].isin(['Alice', 'Bob']))
    assert all(df['Gender'] == 'Other')

def test_task_func_custom_age_and_score_ranges():
    df = task_func(3, age_range=(20, 25), score_range=(80, 90))
    assert all(df['Age'].between(20, 25))
    assert all(df['Score'].between(80, 90))

def test_task_func_reproducibility():
    df1 = task_func(3, seed=42)
    df2 = task_func(3, seed=42)
    assert df1.equals(df2)

def test_task_func_large_number_of_students():
    df = task_func(100)
    assert len(df) == 100
    assert list(df.columns) == ['Name', 'Age', 'Gender', 'Score']
    assert all(df['Age'].between(15, 20))
    assert all(df['Score'].between(50, 100))