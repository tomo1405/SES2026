import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0431 import task_func

# Mock data for testing
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature1': [1.0, 2.0, 3.0, 4.0]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature2': [5.0, 6.0, 7.0, 8.0]
})

def test_task_func():
    labels, ax = task_func(df1, df2, column1="feature1", column2="feature2")
    
    # Check that labels is a numpy array of shape (n_samples,)
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (4,)
    
    # Check that ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)
    
    # Check that the scatter plot has the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 4
    assert len(ydata) == 4
    
    # Check that the labels are within the expected range
    assert np.all(np.isin(labels, [0, 1]))

# Run the tests
if __name__ == "__main__":
    pytest.main()