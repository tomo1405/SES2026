import pandas as pd
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
import pytest

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['A', 'B', 'C']
    target_column = 'C'
    with pytest.raises(ValueError):
        task_func(data, columns, target_column)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['A', 'B', 'C']
    target_column = 'D'
    with pytest.raises(ValueError):
        task_func(data, columns, target_column)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['A', 'B', 'C']
    target_column = 'C'
    accuracy = task_func(data, columns, target_column)
    assert accuracy == 1.0