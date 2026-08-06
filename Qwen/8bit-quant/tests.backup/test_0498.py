import pytest
from src_0498 import task_func
from datetime import datetime, timedelta
import pytz
import calendar

def test_task_func_default_days():
    # Arrange
    expected_weekday = calendar.day_name[(datetime.now(pytz.UTC) - timedelta(days=7)).weekday()]
    
    # Act
    result = task_func()
    
    # Assert
    assert result == expected_weekday

def test_task_func_custom_days():
    # Arrange
    days_in_past = 5
    expected_weekday = calendar.day_name[(datetime.now(pytz.UTC) - timedelta(days=days_in_past)).weekday()]
    
    # Act
    result = task_func(days_in_past)
    
    # Assert
    assert result == expected_weekday

def test_task_func_negative_days():
    # Arrange
    days_in_past = -1
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        task_func(days_in_past)
    assert str(excinfo.value) == "Days in the past cannot be negative"

def test_task_func_zero_days():
    # Arrange
    days_in_past = 0
    expected_weekday = calendar.day_name[datetime.now(pytz.UTC).weekday()]
    
    # Act
    result = task_func(days_in_past)
    
    # Assert
    assert result == expected_weekday