import pytest
from src_0100 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    fig = task_func()
    
    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object."
    
    # Check if the figure has a title
    assert fig.axes[0].get_title() == 'Iris Dataset Pair Plot', "The figure should have the correct title."
    
    # Check if there are 6 subplots (2x3 grid for pairplot of 4 features)
    assert len(fig.axes) == 6, "The figure should contain 6 subplots."
    
    # Check if each subplot has the correct x and y labels
    expected_labels = [
        ('sepal length (cm)', 'sepal length (cm)'),
        ('sepal width (cm)', 'sepal length (cm)'),
        ('petal length (cm)', 'sepal length (cm)'),
        ('petal width (cm)', 'sepal length (cm)'),
        ('sepal length (cm)', 'sepal width (cm)'),
        ('sepal width (cm)', 'sepal width (cm)')
    ]
    
    for i, (ax, (xlabel, ylabel)) in enumerate(zip(fig.axes, expected_labels)):
        assert ax.get_xlabel() == xlabel, f"Subplot {i} should have the correct x label."
        assert ax.get_ylabel() == ylabel, f"Subplot {i} should have the correct y label."

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])