import pytest
from src_0981 import task_func

def test_task_func():
    # Mock input data
    df = ...

    # Call the function
    result = task_func(df)

    # Assert the expected output
    assert result[0] is not None
    assert result[1] is not None
    assert isinstance(result[0], pd.DataFrame)
    assert isinstance(result[1], plt.Figure)