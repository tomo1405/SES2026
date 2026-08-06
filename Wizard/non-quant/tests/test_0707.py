python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def task_func(data, columns, target_column):
    df = pd.DataFrame(data, columns=columns)
    if target_column not in df.columns:
        raise ValueError('Target column does not exist in DataFrame')

    X = df.drop(columns=target_column)  # Operate directly on the DataFrame
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

def test_task_func():
    data = [
        {'name': 'Alice', 'age': 25, 'gender': 'female', 'income': 50000},
        {'name': 'Bob', 'age': 30, 'gender': 'male', 'income': 60000},
        {'name': 'Charlie', 'age': 35, 'gender': 'male', 'income': 70000},
        {'name': 'Dave', 'age': 40, 'gender': 'male', 'income': 80000},
        {'name': 'Eve', 'age': 45, 'gender': 'female', 'income': 90000},
    ]
    columns = ['name', 'age', 'gender', 'income']
    target_column = 'gender'

    accuracy = task_func(data, columns, target_column)

    assert accuracy == 1.0

def test_task_func_invalid_target_column():
    data = [
        {'name': 'Alice', 'age': 25, 'gender': 'female', 'income': 50000},
        {'name': 'Bob', 'age': 30, 'gender': 'male', 'income': 60000},
        {'name': 'Charlie', 'age': 35, 'gender': 'male', 'income': 70000},
        {'name': 'Dave', 'age': 40, 'gender': 'male', 'income': 80000},
        {'name': 'Eve', 'age': 45, 'gender': 'female', 'income': 90000},
    ]
    columns = ['name', 'age', 'gender', 'income']
    target_column = 'salary'

    with pytest.raises(ValueError):
        task_func(data, columns, target_column)