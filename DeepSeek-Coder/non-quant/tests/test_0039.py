import pytest
from src_0039 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample data matrix
    data_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    expected_df = pd.DataFrame({
        "Feature 1": [-1.264911, -1.264911, -1.264911],
        "Feature 2": [-0.848528, -0.848528, -0.848528],
        "Feature 3": [-0.432145, -0.432145, -0.432145],
        "Feature 4": [-0.015762, -0.015762, -0.015762],
        "Feature 5": [0.400621, 0.400621, 0.400621],
        "Mean": [2.0, 7.0, 12.0]
    })
    expected_df, _ = task_func(data_matrix)
    pd.testing.assert_frame_equal(expected_df, expected_df)

    # Check if the plot is created and displayed
    assert plt.gcf().canvas.get_renderer()._renderer_class_()._axes == 1

if __name__ == "__main__":
    pytest.main()