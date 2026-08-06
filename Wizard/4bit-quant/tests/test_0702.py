python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0702 import task_func

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    target = 'c'
    expected_score = 1.0
    
    model = LinearRegression()
    model.fit(df.drop(target, axis=1), df[target])
    actual_score = model.score(df.drop(target, axis=1), df[target])
    
    assert actual_score == expected_score