import numpy as np
from src_0094 import task_func


def test_task_func():
    data = np.random.rand(100, 10)
    n_components = 3
    expected_columns = [f'PC{i+1}' for i in range(n_components)]
    expected_data = np.random.rand(100, n_components)
    expected_ax = None  # You can replace this with the expected value of the ax object

    df, ax = task_func(data, n_components)

    assert df.columns.tolist() == expected_columns
    assert df.values.tolist() == expected_data.tolist()
    assert ax == expected_ax