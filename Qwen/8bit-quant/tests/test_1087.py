import pytest
from src_1087 import task_func

def test_task_func():
    df = task_func()
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == 1000, "The DataFrame should have 1000 rows."
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ["String Field", "Float Field"], "The DataFrame should have two columns: 'String Field' and 'Float Field'."
    
    # Check if 'String Field' contains strings of length 10
    for s in df["String Field"]:
        assert isinstance(s, str), "Each element in 'String Field' should be a string."
        assert len(s) == 10, "Each string in 'String Field' should have a length of 10."
    
    # Check if 'Float Field' contains formatted float strings
    for f in df["Float Field"]:
        assert isinstance(f, str), "Each element in 'Float Field' should be a string."
        assert f.count(',') <= 3, "Each string in 'Float Field' should have at most 3 commas (for thousands separator)."
        assert f.count('.') == 1, "Each string in 'Float Field' should have exactly one decimal point."
        assert len(f.split('.')[1]) == 2, "Each string in 'Float Field' should have exactly 2 digits after the decimal point."