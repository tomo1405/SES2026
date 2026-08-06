python
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import pytest

from src_0665 import task_func

@pytest.fixture
def sales_data():
    sales_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Sales1': [100, 120, 150, 200, 220, 250, 300, 320, 350, 400, 420, 450],
        'Sales2': [110, 130, 160, 210, 230, 260, 310, 330, 360, 410, 430, 460],
        'Sales3': [120, 140, 170, 220, 240, 270, 320, 340, 370, 420, 440, 470]
    })
    return sales_data

def test_task_func(sales_data):
    ax = task_func(sales_data)
    assert isinstance(ax, plt.Axes)