import pytest
from src_0804 import task_func

def test_task_func():
    # Test that the function raises an error when the input file has no numeric columns
    with pytest.raises(ValueError):
        task_func('test_data.csv')

    # Test that the function returns a DataFrame with the expected columns
    expected_columns = ['a', 'b', 'c']
    df = task_func('test_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == expected_columns

    # Test that the function scales the numeric columns correctly
    expected_scaling = [0.5, 0.75, 1.0]
    df = task_func('test_data.csv')
    assert np.allclose(df['a'], expected_scaling)
    assert np.allclose(df['b'], expected_scaling)
    assert np.allclose(df['c'], expected_scaling)