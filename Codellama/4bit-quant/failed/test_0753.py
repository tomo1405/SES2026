import pytest
from src_0753 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    test_size = 0.2
    random_state = 0

    # Test 1: data is not a DataFrame
    with pytest.raises(ValueError):
        task_func(data=1, target_column=target_column, test_size=test_size, random_state=random_state)

    # Test 2: data is empty
    with pytest.raises(ValueError):
        task_func(data=pd.DataFrame(), target_column=target_column, test_size=test_size, random_state=random_state)

    # Test 3: target_column is not in data
    with pytest.raises(ValueError):
        task_func(data=data, target_column='D', test_size=test_size, random_state=random_state)

    # Test 4: data values are not numeric
    with pytest.raises(ValueError):
        task_func(data=pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3], 'C': [4, 5, 6]}), target_column=target_column, test_size=test_size, random_state=random_state)

    # Test 5: test_size is not between 0 and 1
    with pytest.raises(ValueError):
        task_func(data=data, target_column=target_column, test_size=-1, random_state=random_state)

    # Test 6: random_state is not an integer
    with pytest.raises(ValueError):
        task_func(data=data, target_column=target_column, test_size=test_size, random_state='a')

    # Test 7: data is valid
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model = LinearRegression().fit(X_train, y_train)
    score = model.score(X_test, y_test)
    assert score > 0