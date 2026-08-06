import pytest
from src_0064 import task_func

def test_task_func():
    car_dict = {
        "Car1": "Red",
        "Car2": "Blue",
        "Car3": "Red",
        "Car4": "Green",
        "Car5": "Blue"
    }
    df, ax = task_func(car_dict)
    
    # Check if DataFrame is created correctly
    expected_columns = ['Car', 'Color']
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check if the DataFrame contains the correct data
    expected_data = [
        ("Car1", "Red"),
        ("Car2", "Blue"),
        ("Car3", "Red"),
        ("Car4", "Green"),
        ("Car5", "Blue")
    ]
    assert df.to_records(index=False).tolist() == expected_data, "DataFrame data is incorrect"
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The returned object is not a matplotlib Axes instance"
    assert ax.get_title() == "Distribution of Vehicle Colors", "Plot title is incorrect"
    assert ax.get_xlabel() == "Color", "Plot x-axis label is incorrect"
    assert ax.get_ylabel() == "Frequency", "Plot y-axis label is incorrect"
    
    # Check if the bar plot data is correct
    color_counts = df["Color"].value_counts()
    bars = ax.patches
    assert len(bars) == len(color_counts), "Number of bars in the plot does not match the number of unique colors"
    
    for bar, (color, count) in zip(bars, color_counts.items()):
        assert bar.get_height() == count, f"Bar height for color {color} is incorrect"