import pytest
from src_0102 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

@pytest.fixture
def mock_data(monkeypatch):
    def mock_read_csv(url, sep, skiprows, header):
        # Mocked data similar to the Boston dataset structure
        data = [
            [0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900, 1, 296.0, 15.3, 396.90, 4.98],
            24.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.02774, 0.0, 7.07, 0, 0.469, 7.185, 41.2, 40.62, 2, 242.0, 17.8, 396.90, 9.14
        ]
        return pd.DataFrame(data=np.array(data).reshape(-1, len(columns)), columns=columns)
    
    columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

@pytest.mark.usefixtures("mock_data")
def test_task_func():
    # Call the function
    ax = task_func()

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."

    # Check if the heatmap is created with the correct number of columns
    assert len(ax.collections) > 0, "The heatmap should have at least one collection."

    # Check if the correlation matrix is computed correctly
    # Since we are using mocked data, we need to manually check the correlation values
    expected_corr = pd.DataFrame({
        'CRIM': [1.0, 0.2492],  # Example correlation values based on the mocked data
        'ZN': [0.2492, 1.0]
    }, index=['CRIM', 'ZN'])

    actual_corr = ax.get_figure().get_axes()[0].collections[0].get_array()
    assert np.allclose(actual_corr, expected_corr.values.flatten()), "The correlation values in the heatmap do not match the expected values."

# Uncomment the following lines to run the test
# if __name__ == "__main__":
#     pytest.main()