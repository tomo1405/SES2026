import pytest
from src_0113 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    with pytest.raises(ValueError):
        df = pd.DataFrame({'Column1': [1, 2, 3]})
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({'Status': ['Active', 'Inactive', 'Active', 'Pending', 'Inactive']})
    ax = task_func(df)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.AxesSubplot)

    # Check if the pie chart has the correct number of segments
    patches, texts, autotexts = ax.pie(df['Status'].value_counts(), labels=df['Status'].value_counts().index, autopct='%1.1f%%')
    assert len(patches) == df['Status'].nunique()

    # Check if the title is set correctly
    assert ax.get_title() == 'Status Distribution'

def test_task_func_plot_output():
    df = pd.DataFrame({'Status': ['Active', 'Inactive', 'Active', 'Pending', 'Inactive']})
    ax = task_func(df)
    
    # Save the plot to a buffer and encode it in base64
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    b64_encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Assert that the image is not empty
    assert b64_encoded_image