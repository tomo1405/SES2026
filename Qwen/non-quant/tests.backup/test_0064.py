import pytest
from src_0064 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Sample input data
    car_dict = {
        'Toyota': 'Red',
        'Honda': 'Blue',
        'Ford': 'Red',
        'Chevrolet': 'Blue',
        'BMW': 'Black'
    }
    
    # Expected DataFrame
    expected_df = pd.DataFrame({
        'Car': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW'],
        'Color': ['Red', 'Blue', 'Red', 'Blue', 'Black']
    })
    
    # Capture the plot output
    plt.ioff()  # Turn off interactive mode to prevent plot display
    df, ax = task_func(car_dict)
    plt.ion()  # Turn on interactive mode back
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Vehicle Colors"
    assert ax.get_xlabel() == "Color"
    assert ax.get_ylabel() == "Frequency"
    
    # Check the bar plot data
    bars = ax.patches
    expected_colors = ['Red', 'Blue', 'Black']
    expected_values = [2, 2, 1]
    
    for i, bar in enumerate(bars):
        assert bar.get_height() == expected_values[i]
        assert bar.get_color() == 'maroon'
    
    # Save the plot to a buffer and check the image content
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    assert len(img_str) > 0  # Ensure the image is not empty