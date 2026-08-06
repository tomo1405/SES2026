import pytest
from src_0946 import task_func

def test_task_func():
    # Test that the function returns the correct type
    assert isinstance(task_func(), np.ndarray)
    
    # Test that the function returns the correct shape
    assert task_func().shape == (2*len(sales_df),)
    
    # Test that the function returns the correct values
    expected_future_sales = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
    assert np.allclose(task_func(), expected_future_sales)