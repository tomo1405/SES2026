python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src_0237 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John', 'Jane'],
                       'Age': [25, 30, 25, 30],
                       'Score': [80, 90, 70, 80],
                       'Category': ['A', 'A', 'B', 'B']})
    accuracy = task_func(df)
    assert accuracy == 1.0
    
    # Test case 2: Test with invalid input (not a DataFrame)
    with pytest.raises(ValueError):
        task_func(123)
    
    # Test case 3: Test with invalid input (duplicate names)
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John', 'Jane'],
                       'Age': [25, 30, 25, 30],
                       'Score': [80, 90, 70, 80],
                       'Category': ['A', 'A', 'B', 'B']})
    with pytest.raises(ValueError):
        task_func(df)