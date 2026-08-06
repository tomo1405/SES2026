import pytest
from src_0309 import task_func

def test_task_func_returns_dataframe():
    df = task_func()
    assert isinstance(df, pd.DataFrame)

def test_task_func_returns_correct_columns():
    df = task_func()
    assert set(df.columns) == set(FIELDS + ['Average Grade'])

def test_task_func_returns_correct_data():
    df = task_func()
    assert all(df['Average Grade'] >= 0) and all(df['Average Grade'] <= 100)

def test_task_func_returns_correct_average_grade():
    df = task_func()
    assert df.loc['Average', 'Average Grade'] == df['Average Grade'].mean()

def test_task_func_returns_correct_average_grades():
    df = task_func()
    assert all(df.loc['Average', FIELDS] == df[FIELDS].mean())

def test_task_func_returns_correct_data_with_additional_fields():
    df = task_func(['Additional Field'])
    assert set(df.columns) == set(FIELDS + ['Average Grade', 'Additional Field'])

def test_task_func_returns_correct_data_with_additional_fields_and_grades():
    df = task_func(['Additional Field'])
    assert all(df['Additional Field'] >= 0) and all(df['Additional Field'] <= 100)

def test_task_func_returns_correct_average_grade_with_additional_fields():
    df = task_func(['Additional Field'])
    assert df.loc['Average', 'Average Grade'] == df['Average Grade'].mean()

def test_task_func_returns_correct_average_grades_with_additional_fields():
    df = task_func(['Additional Field'])
    assert all(df.loc['Average', FIELDS] == df[FIELDS].mean())

def test_task_func_returns_correct_average_grades_with_additional_fields_and_grades():
    df = task_func(['Additional Field'])
    assert all(df.loc['Average', FIELDS + ['Additional Field']] == df[FIELDS + ['Additional Field']].mean())