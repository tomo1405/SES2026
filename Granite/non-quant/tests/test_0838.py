import pytest
from src_0838 import task_func

def test_task_func():
    # Test case 1: Test with default arguments
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (100, 5)
    assert result.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    
    # Test case 2: Test with custom arguments
    result = task_func(n_rows=50, scale_cols=[0, 2], columns=['X', 'Y', 'Z'])
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (50, 3)
    assert result.columns.tolist() == ['X', 'Y', 'Z']
    assert result['X'].dtype == 'float64'
    assert result['Y'].dtype == 'float64'
    assert result['Z'].dtype == 'int64'
    
    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(n_rows=-1, scale_cols=[0, 2])
    with pytest.raises(TypeError):
        task_func(n_rows=50, scale_cols=[0, 2], columns='ABC')