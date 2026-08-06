import pytest
from src_0104 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_with_empty_dataframe():
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(temperatures)
    assert str(excinfo.value) == "Input temperatures must be a non-empty pandas DataFrame."

def test_task_func_with_non_dataframe_input():
    temperatures = [1, 2, 3]
    with pytest.raises(ValueError) as excinfo:
        task_func(temperatures)
    assert str(excinfo.value) == "Input temperatures must be a non-empty pandas DataFrame."

def test_task_func_with_valid_data():
    data = {
        'temperature': [15, 16, 17, 18, 19]
    }
    index = pd.date_range(start='2023-01-01', periods=5)
    temperatures = pd.DataFrame(data, index=index)
    
    ax = task_func(temperatures)
    
    # Check if the plot is created correctly
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 5
    assert len(ax.lines[0].get_ydata()) == 5

    # Clean up
    plt.close(fig=ax.figure)