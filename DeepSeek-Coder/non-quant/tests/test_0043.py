import pytest
from src_0043 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Define test cases
def test_task_func():
    # Test with a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_df = pd.DataFrame({
        "Component 1": [-2.5667, -2.5667, -2.5667],
        "Component 2": [0.8485, 0.8485, 0.8485],
        "Mean": [2.0, 5.0, 8.0]
    })
    expected_df = expected_df.astype(float)

    df, ax = task_func(data_matrix)

    # Check the DataFrame
    pd.testing.assert_frame_equal(df, expected_df)

    # Check the plot
    assert ax is not None
    plt.close()

# Run the test
if __name__ == "__main__":
    pytest.main()