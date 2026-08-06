import pytest
from src_0660 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    x = [np.linspace(-3, 3, 100), np.linspace(-2, 2, 100)]
    y = [np.random.normal(0, 1, 100), np.random.normal(1, 2, 100)]
    labels = ['Normal(0, 1)', 'Normal(1, 2)']
    return x, y, labels

def test_task_func(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    
    # Check if the figure is an instance of plt.Figure
    assert isinstance(fig, plt.Figure)
    
    # Check if the number of axes matches the expected number
    assert len(fig.axes) == 1
    
    # Check if the legend has the correct number of labels
    legend_labels = [text.get_text() for text in fig.axes[0].get_legend().get_texts()]
    assert set(legend_labels) == set(labels)

# Run the tests
if __name__ == "__main__":
    pytest.main()