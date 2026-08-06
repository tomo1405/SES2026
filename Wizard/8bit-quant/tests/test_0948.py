python
import numpy as np
import random
from datetime import datetime
import pytest

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Convert start_date and end_date to numpy datetime64 objects
    if seed is not None:
        random.seed(seed)
    
    # Convert start_date and end_date to numpy datetime64 objects
    start_date_np = np.datetime64(start_date)
    end_date_np = np.datetime64(end_date)

    # Calculate the number of days between start_date and end_date
    total_days = int((end_date_np - start_date_np).astype('timedelta64[D]').astype(int) + 1)

    # Randomly select unique dates within the range without replacement using random.sample
    selected_dates = sorted(random.sample(range(total_days), rows * columns))

    # Generate the matrix with selected unique dates
    matrix = (start_date_np + np.array(selected_dates).astype('timedelta64[D]')).reshape(rows, columns)

    return matrix

def test_task_func():
    # Test case 1: Test with default arguments
    matrix = task_func()
    assert matrix.shape == (3, 2)
    assert matrix.dtype == np.dtype('datetime64[D]')
    assert (matrix[0, :] == np.array(['2021-01-01', '2021-01-02'], dtype='datetime64[D]')).all()
    assert (matrix[1, :] == np.array(['2021-01-03', '2021-01-04'], dtype='datetime64[D]')).all()
    assert (matrix[2, :] == np.array(['2021-01-05', '2021-01-06'], dtype='datetime64[D]')).all()

    # Test case 2: Test with custom arguments
    matrix = task_func(rows=2, columns=3, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31), seed=1)
    assert matrix.shape == (2, 3)
    assert matrix.dtype == np.dtype('datetime64[D]')
    assert (matrix[0, :] == np.array(['2022-01-01', '2022-01-02', '2022-01-03'], dtype='datetime64[D]')).all()
    assert (matrix[1, :] == np.array(['2022-01-04', '2022-01-05', '2022-01-06'], dtype='datetime64[D]')).all()

    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(rows=0)
    with pytest.raises(ValueError):
        task_func(columns=0)
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2022, 1, 1), end_date=datetime(2021, 1, 1))
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2022, 2, 29), end_date=datetime(2022, 3, 1))