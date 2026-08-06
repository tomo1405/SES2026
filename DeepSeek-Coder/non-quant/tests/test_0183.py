import pytest
from src_0183 import task_func
import pandas as pd

# Mock data for testing
data = {
    'Title': ['How to learn Python', 'What is Data Science', 'Python Programming'],
    'Content': ['Learn Python now', 'Data Science is important', 'Programming in Python']
}
df = pd.DataFrame(data)

def test_task_func():
    result = task_func(df)
    assert isinstance(result, list), "The result should be a list"
    assert len(result) > 0, "The result list should not be empty"
    assert all(isinstance(label, int) for label in result), "All labels should be integers"