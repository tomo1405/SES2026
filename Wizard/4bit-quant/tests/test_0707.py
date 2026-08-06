python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src_0707 import task_func

def test_task_func():
    data = [
        {'name': 'John', 'age': 25, 'gender': 'male', 'income': 50000},
        {'name': 'Jane', 'age': 30, 'gender': 'female', 'income': 60000},
        {'name': 'Bob', 'age': 40, 'gender': 'male', 'income': 70000},
        {'name': 'Alice', 'age': 35, 'gender': 'female', 'income': 55000},
        {'name': 'Tom', 'age': 28, 'gender': 'male', 'income': 45000},
        {'name': 'Mary', 'age': 32, 'gender': 'female', 'income': 65000},
    ]
    columns = ['name', 'age', 'gender', 'income']
    target_column = 'gender'

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

    assert accuracy == task_func(data, columns, target_column)