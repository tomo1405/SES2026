import pytest
from src_0118 import task_func

def test_task_func_positive_num_of_students():
    num_of_students = 10
    df = task_func(num_of_students)
    assert len(df) == num_of_students

def test_task_func_negative_num_of_students():
    num_of_students = -1
    with pytest.raises(ValueError):
        task_func(num_of_students)

def test_task_func_custom_name_list():
    num_of_students = 10
    name_list = ['Alice', 'Bob', 'Charlie']
    df = task_func(num_of_students, name_list=name_list)
    assert len(df) == num_of_students
    assert all(df['Name'].isin(name_list))

def test_task_func_custom_gender_list():
    num_of_students = 10
    gender_list = ['Female', 'Male']
    df = task_func(num_of_students, gender_list=gender_list)
    assert len(df) == num_of_students
    assert all(df['Gender'].isin(gender_list))

def test_task_func_custom_age_range():
    num_of_students = 10
    age_range = (10, 20)
    df = task_func(num_of_students, age_range=age_range)
    assert len(df) == num_of_students
    assert all(df['Age'].between(age_range[0], age_range[1]))

def test_task_func_custom_score_range():
    num_of_students = 10
    score_range = (50, 100)
    df = task_func(num_of_students, score_range=score_range)
    assert len(df) == num_of_students
    assert all(df['Score'].between(score_range[0], score_range[1]))

def test_task_func_custom_seed():
    num_of_students = 10
    seed = 1234
    df1 = task_func(num_of_students, seed=seed)
    df2 = task_func(num_of_students, seed=seed)
    assert df1.equals(df2)