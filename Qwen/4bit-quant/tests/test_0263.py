import pytest
from src_0263 import task_func
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import io
import matplotlib.figure

def test_task_func():
    # Create a mock dictionary and new key-value pair
    initial_dict = {'a': 1, 'b': 2}
    new_key = 'c'
    new_value = 3
    
    # Call the function
    result_dict, ax = task_func(initial_dict.copy(), new_key, new_value)
    
    # Check if the new key-value pair is added correctly
    assert result_dict == {'a': 1, 'b': 2, 'c': 3}
    
    # Check if the plot is created correctly
    assert isinstance(ax, sns.axisgrid.BarPlotter)
    
    # Capture the plot output to check if it's generated
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.read()  # This will raise an assertion error if the buffer is empty

    # Clean up the plot to avoid interference with other tests
    plt.close()