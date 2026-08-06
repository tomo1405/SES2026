import pytest
from src_0301 import task_func
import pandas as pd
import numpy as np
from io import StringIO

def test_task_func():
    # Create a sample DataFrame
    data = StringIO("""
Date,Value
2021-01-01,[1,2,3]
2021-01-02,[4,5,6]
2021-01-03,[7,8,9]
""")
    df = pd.read_csv(data)

    # Call the function
    result_df, fig = task_func(df)

    # Check the result DataFrame
    expected_columns = ['Date', 0, 1, 2]
    assert list(result_df.columns) == expected_columns

    # Check that 'Date' column is datetime
    assert pd.api.types.is_datetime64_any_dtype(result_df['Date'])

    # Check that z-scores are calculated correctly
    expected_zscores = np.array([
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]
    ])
    np.testing.assert_array_almost_equal(result_df.iloc[:, 1:].values, expected_zscores)

    # Check that the figure is created
    assert isinstance(fig, plt.Figure)

    # Check that the plot has the correct title and labels
    ax = fig.axes[0]
    assert ax.get_title() == 'Z-Scores Over Time'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Z-Score'

# Run the tests
if __name__ == "__main__":
    pytest.main()