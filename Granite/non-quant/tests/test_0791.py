import pytest
from src_0791 import task_func

def test_task_func():
    df = ...  # Provide a sample DataFrame for testing
    col1 = ...  # Provide a sample column name for testing
    col2 = ...  # Provide a sample column name for testing
    N = ...  # Provide a sample value for N

    with pytest.raises(ValueError):
        task_func(df, "invalid_col1", col2, N)
    with pytest.raises(ValueError):
        task_func(df, col1, "invalid_col2", N)
    with pytest.raises(ValueError):
        task_func(df, "invalid_col1", "invalid_col2", N)

    result = task_func(df, col1, col2, N)
    assert isinstance(result, list)
    assert len(result) == N
    for i in result:
        assert i in df.index