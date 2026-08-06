import pytest
from src_1026 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test with a non-empty dictionary
    data_dict = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    expected_df = pd.DataFrame(data_dict)
    expected_df_scaled = expected_df.copy()
    expected_df_scaled = expected_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

    result_df, ax = task_func(data_dict)

    assert result_df.equals(expected_df_scaled), "The scaled DataFrame does not match the expected result."
    assert ax.get_title() == "Scaled Values", "The plot title does not match the expected title."

    # Test with an empty dictionary
    empty_data_dict = {}
    result_df, ax = task_func(empty_data_dict)
    assert result_df.empty, "Expected an empty DataFrame when input is empty."
    assert ax is None, "Expected no plot to be generated for an empty input."

    print("All tests passed.")