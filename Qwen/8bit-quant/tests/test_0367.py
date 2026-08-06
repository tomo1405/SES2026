import pytest
from src_0367 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def number_list():
    return np.random.randint(0, 100, size=50)

@pytest.fixture
def bins():
    return 10

def test_task_func(number_list, bins):
    ax = task_func(number_list, bins)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."
    
    # Check if the histogram has the correct number of bins
    n, bins, patches = ax.hist(number_list, bins=bins)
    assert len(bins) == bins + 1, f"The histogram should have {bins + 1} bins."
    
    # Check if the title and labels are set correctly
    assert ax.get_title() == 'Histogram', "The title should be 'Histogram'."
    assert ax.get_xlabel() == 'Number', "The x-label should be 'Number'."
    assert ax.get_ylabel() == 'Frequency', "The y-label should be 'Frequency'."
    
    # Check if the color is one of the predefined colors
    color = patches[0].get_facecolor()
    assert any(color == [int(c.lstrip('#')[i:i+2], 16)/255.0 for i in (0, 2, 4)]) for c in ['#00bfbf', '#000000', '#0000ff']), "The color should be one of the predefined colors."