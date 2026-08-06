import pytest
from src_0640 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2
    
    # Test that the first element is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)
    
    # Test that the second element is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)
    
    # Test that the DataFrame has the correct shape
    assert df.shape == (100, 5)
    
    # Test that the DataFrame has the correct column names
    assert list(df.columns) == ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5']
    
    # Test that the DataFrame has the correct index names
    assert list(df.index) == ['Sample1', 'Sample2', 'Sample3', 'Sample4', 'Sample5']
    
    # Test that the heatmap has the correct shape
    assert ax.shape == (5, 5)
    
    # Test that the heatmap has the correct labels
    assert ax.xlabel == 'Feature'
    assert ax.ylabel == 'Sample'
    
    # Test that the heatmap has the correct values
    assert ax.values == df.corr()