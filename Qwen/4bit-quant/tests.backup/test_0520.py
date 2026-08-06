import pytest
from src_0520 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Sample data for testing
    data = {
        'Apple': [10, 20, 30, 40],
        'Banana': [15, 25, 35, 45],
        'Cherry': [5, 10, 15, 20]
    }
    
    # Call the function with the sample data
    ax = task_func(data)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == "Time", "X-axis label should be 'Time'"
    assert ax.get_ylabel() == "Sales Quantity", "Y-axis label should be 'Sales Quantity'"
    assert ax.get_title() == "Fruit Sales over Time", "Plot title should be 'Fruit Sales over Time'"
    
    # Check if the legend is present
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert set(legend_labels) == {'Apple', 'Banana', 'Cherry'}, "Legend should include all fruits"

    # Check if the data is plotted correctly
    lines = ax.get_lines()
    assert len(lines) == 3, "There should be one line for each fruit"
    for i, fruit in enumerate(['Apple', 'Banana', 'Cherry']):
        assert list(lines[i].get_ydata()) == data[fruit], f"Data for {fruit} is incorrect"

    # Save the plot to a buffer and check its content
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert len(img_str) > 0, "The plot image should not be empty"

# Run the tests
if __name__ == "__main__":
    pytest.main()