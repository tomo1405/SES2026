import pytest
from src_0492 import task_func
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io

def test_task_func_invalid_epoch_milliseconds():
    with pytest.raises(ValueError, match="Start time cannot be negative."):
        task_func(-1000)

def test_task_func_start_date_after_current_time():
    epoch_milliseconds = int((datetime.utcnow() + timedelta(days=1)).timestamp()) * 1000
    with pytest.raises(ValueError, match="Start date must be before current time."):
        task_func(epoch_milliseconds)

def test_task_func_valid_input():
    epoch_milliseconds = int((datetime.utcnow() - timedelta(days=1)).timestamp()) * 1000
    sales_data, ax = task_func(epoch_milliseconds, seed=42)
    assert len(sales_data) == 5  # 5 categories
    for category, sales in sales_data.items():
        assert len(sales) == 1  # 1 day difference
        assert 10 <= sales[0] <= 50  # Sales within the expected range

    # Check if the plot was created correctly
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue()  # Ensure the buffer is not empty

def test_task_func_with_seed():
    epoch_milliseconds = int((datetime.utcnow() - timedelta(days=1)).timestamp()) * 1000
    sales_data_1, _ = task_func(epoch_milliseconds, seed=42)
    sales_data_2, _ = task_func(epoch_milliseconds, seed=42)
    assert sales_data_1 == sales_data_2  # Same seed should produce same results