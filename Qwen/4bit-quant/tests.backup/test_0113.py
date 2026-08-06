import pytest
from src_0113 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_input_validation():
    # Test with non-DataFrame input
    with pytest.raises(ValueError, match="Input must be a pandas DataFrame with a 'Status' column."):
        task_func([1, 2, 3])

    # Test with DataFrame missing 'Status' column
    df = pd.DataFrame({'Name': ['Alice', 'Bob']})
    with pytest.raises(ValueError, match="Input must be a pandas DataFrame with a 'Status' column."):
        task_func(df)

def test_task_func_pie_chart():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Status': ['Active', 'Inactive', 'Active', 'Pending', 'Inactive']
    })

    # Call the function and capture the plot
    ax = task_func(df)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Status Distribution'

    # Capture the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Define the expected base64 string (this should be pre-defined or generated once)
    expected_image_base64 = "your_expected_base64_string_here"

    # Assert that the generated image matches the expected one
    assert image_base64 == expected_image_base64