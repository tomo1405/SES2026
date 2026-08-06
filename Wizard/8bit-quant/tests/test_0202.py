python
import bisect
import statistics
import pytest
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, column, value):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in DataFrame")
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")

    data = df[column].values
    avg = statistics.mean(data)
    greater_avg = data[data > avg]
    
    data.sort()
    bpoint = bisect.bisect_right(data, value)
    num_greater_value = len(data) - bpoint
    
    ax = df.hist(column=column, bins=10)[0][0]
    # plt.show()
    
    return greater_avg, num_greater_value, ax

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
    greater_avg, num_greater_value, ax = task_func(df, 'A', 3)
    assert greater_avg.tolist() == [4]
    assert num_greater_value == 1
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of A'
    
    with pytest.raises(ValueError):
        task_func(df, 'C', 3)
        
    with pytest.raises(ValueError):
        task_func(df, 'A', '3')
        
    with pytest.raises(ValueError):
        task_func(df, 'A', 10)