import pandas as pd
from src_0430 import task_func


def test_task_func():
    # Test case 1: Merge dataframes based on 'id'
    df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30], 'feature2': [100, 200, 300]})
    df2 = pd.DataFrame({'id': [1, 2, 3], 'target': [0, 1, 0]})
    expected_merged_df = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30], 'feature2': [100, 200, 300], 'target': [0, 1, 0]})
    assert pd.testing.assert_frame_equal(task_func(df1, df2), expected_merged_df)

    # Test case 2: Separate features and target
    df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30], 'feature2': [100, 200, 300], 'target': [0, 1, 0]})
    expected_X = pd.DataFrame({'feature1': [10, 20, 30], 'feature2': [100, 200, 300]})
    expected_y = pd.Series([0, 1, 0])
    assert pd.testing.assert_frame_equal(task_func(df1, df2)[0], expected_X)
    assert pd.testing.assert_series_equal(task_func(df1, df2)[1], expected_y)

    # Test case 3: Select top 2 features
    df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30], 'feature2': [100, 200, 300], 'feature3': [1000, 2000, 3000], 'target': [0, 1, 0]})
    expected_X_new = pd.DataFrame({'feature1': [10, 20, 30], 'feature2': [100, 200, 300]})
    assert pd.testing.assert_frame_equal(task_func(df1, df2)[0], expected_X_new)

    # Test case 4: Draw heatmap
    df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30], 'feature2': [100, 200, 300], 'feature3': [1000, 2000, 3000], 'target': [0, 1, 0]})
    expected_heatmap = pd.DataFrame({'feature1': [10, 20, 30], 'feature2': [100, 200, 300]})
    assert pd.testing.assert_frame_equal(task_func(df1, df2)[1], expected_heatmap)