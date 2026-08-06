import pytest
from src_0492 import task_func
from datetime import datetime, timedelta

def test_task_func_negative_epoch():
    with pytest.raises(ValueError, match="Start time cannot be negative."):
        task_func(-1000)

def test_task_func_future_start_time():
    epoch_milliseconds = int((datetime.utcnow() + timedelta(days=1)).timestamp()) * 1000
    with pytest.raises(ValueError, match="Start date must be before current time."):
        task_func(epoch_milliseconds)

def test_task_func_with_seed():
    epoch_milliseconds = int(datetime.utcnow().timestamp()) * 1000
    sales_data1, _ = task_func(epoch_milliseconds, seed=42)
    sales_data2, _ = task_func(epoch_milliseconds, seed=42)
    assert sales_data1 == sales_data2

def test_task_func_without_seed():
    epoch_milliseconds = int(datetime.utcnow().timestamp()) * 1000
    sales_data1, _ = task_func(epoch_milliseconds)
    sales_data2, _ = task_func(epoch_milliseconds)
    assert sales_data1 != sales_data2

def test_task_func_categories():
    epoch_milliseconds = int(datetime.utcnow().timestamp()) * 1000
    sales_data, _ = task_func(epoch_milliseconds)
    assert set(sales_data.keys()) == {"Electronics", "Clothing", "Home", "Books", "Sports"}

def test_task_func_sales_range():
    epoch_milliseconds = int(datetime.utcnow().timestamp()) * 1000
    sales_data, _ = task_func(epoch_milliseconds)
    for category, sales in sales_data.items():
        for sale in sales:
            assert 10 <= sale <= 50