import pandas as pd
import pytest
from sklearn.exceptions import NotFittedError
from src_0237 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_no_duplicates():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice'],
        'Age': [25, 30, 25],
        'Score': [85, 90, 85],
        'Category': ['A', 'B', 'A']
    })
    df = df.drop_duplicates(subset='Name')
    assert len(df) == 2

def test_task_func_accuracy():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95],
        'Category': ['A', 'B', 'C']
    })
    accuracy = task_func(df)
    assert 0 <= accuracy <= 1

def test_task_func_model_not_fitted():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95],
        'Category': ['A', 'B', 'C']
    })
    model = RandomForestClassifier(random_state=42)
    X = df[['Age', 'Score']]
    y = df['Category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    with pytest.raises(NotFittedError):
        model.predict(X_test)

def test_task_func_default_parameters():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95],
        'Category': ['A', 'B', 'C']
    })
    accuracy = task_func(df)
    assert accuracy == task_func(df, test_size=0.2, random_state=42)