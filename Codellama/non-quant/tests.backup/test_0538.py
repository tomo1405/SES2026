import pytest
from src_0538 import task_func

def test_task_func():
    # Test that the function raises a ValueError when the data contains negative age values
    with pytest.raises(ValueError):
        task_func(db_name="test.db", table_name="People", age=-1)

    # Test that the function returns a valid Seaborn histogram when the data is valid
    ax = task_func(db_name="test.db", table_name="People", age=10)
    assert isinstance(ax, sns.histplot)
    assert ax.get_xlabel() == "age"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of age"