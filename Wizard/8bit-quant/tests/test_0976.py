python
import pytest
from src_0976 import task_func

def test_task_func():
    # Test case 1: Test with default arguments
    df = task_func(10)
    assert df.shape == (10, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]
    assert df.notna().all().all()

    # Test case 2: Test with custom arguments
    df = task_func(5, columns=["X", "Y", "Z"], seed=1)
    assert df.shape == (5, 3)
    assert list(df.columns) == ["X", "Y", "Z"]
    assert df.notna().all().all()

    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(10, columns=["A", "B", "C", "D", "E", "F"])
    with pytest.raises(ValueError):
        task_func(10, columns=["A", "B", "C", "D", "E", "E"])
    with pytest.raises(ValueError):
        task_func(10, columns=["A", "B", "C", "D", "E", "E"], seed=-1)