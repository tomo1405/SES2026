import pytest
from src_0069 import task_func

def test_task_func():
    # Test with valid data
    data = '/path/to/data.csv'
    emp_prefix = 'EMP'
    df, ax = task_func(data, emp_prefix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axis.Axis)
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    assert ax.shape[0] > 0
    assert ax.shape[1] > 0

    # Test with invalid data
    data = '/path/to/invalid_data.csv'
    emp_prefix = 'EMP'
    with pytest.raises(ValueError):
        task_func(data, emp_prefix)

    # Test with invalid emp_prefix
    data = '/path/to/data.csv'
    emp_prefix = 'INVALID'
    with pytest.raises(ValueError):
        task_func(data, emp_prefix)