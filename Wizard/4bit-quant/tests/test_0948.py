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
    assert matrix.dtype == np.datetime64

    # Test case 2: Test with custom arguments
    matrix = task_func(rows=4, columns=3, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31), seed=1)
    assert matrix.shape == (4, 3)
    assert matrix.dtype == np.datetime64

    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        matrix = task_func(rows=0, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0)

    with pytest.raises(ValueError):
        matrix = task_func(rows=3, columns=0, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0)

    with pytest.raises(ValueError):
        matrix = task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 30), seed=0)

    with pytest.raises(ValueError):
        matrix = task_func(rows=3, columns=2, start_date=datetime(2021, 1, 2), end_date=datetime(2021, 12, 31), seed=0)

    with pytest.raises(ValueError):
        matrix = task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=-1)