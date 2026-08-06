import pytest
from src_0293 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, 40, 45],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Call the function
    df_grouped, (hist, bins) = task_func(df)

    # Check if the returned DataFrame has the correct shape
    assert df_grouped.shape == (4, 2), "The grouped DataFrame should have 4 rows and 2 columns."

    # Check if the returned histogram and bins are correct
    expected_hist, expected_bins = np.histogram([0.25, 0.33333333, 0.5, 0.66666667], bins=10)
    assert np.array_equal(hist, expected_hist), "The histogram does not match the expected values."
    assert np.allclose(bins, expected_bins), "The bins do not match the expected values."

    # Check if the scaling is applied correctly
    assert df_grouped.loc[df_grouped['id'] == 1, 'age'].iloc[0] == 0.25, "The first age value should be scaled to 0.25."
    assert df_grouped.loc[df_grouped['id'] == 1, 'income'].iloc[0] == 0.33333333, "The first income value should be scaled to 0.33333333."
    assert df_grouped.loc[df_grouped['id'] == 2, 'age'].iloc[0] == 0.5, "The second age value should be scaled to 0.5."
    assert df_grouped.loc[df_grouped['id'] == 2, 'income'].iloc[0] == 0.66666667, "The second income value should be scaled to 0.66666667."

# Run the tests
if __name__ == "__main__":
    pytest.main()