import pytest
from src_0496 import task_func

def test_task_func():
    result = task_func(days=10, random_seed=42)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert "date" in result.columns, "The DataFrame should have a 'date' column"
    assert "Groceries" in result.columns, "The DataFrame should have 'Groceries' column"
    assert "Entertainment" in result.columns, "The DataFrame should have 'Entertainment' column"
    assert "Rent" in result.columns, "The DataFrame should have 'Rent' column"
    assert "Utilities" in result.columns, "The DataFrame should have 'Utilities' column"
    assert "Miscellaneous" in result.columns, "The DataFrame should have 'Miscellaneous' column"
    assert len(result) == 10, "The DataFrame should have 10 rows"