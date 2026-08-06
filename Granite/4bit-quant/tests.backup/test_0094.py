import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from src_0094 import task_func

def test_task_func():
    data = np.random.rand(100, 10)
    n_components = 2
    expected_columns = [f'PC{i+1}' for i in range(n_components)]
    expected_data = pd.DataFrame(np.random.rand(100, n_components), columns=expected_columns)
    expected_ax = plt.axes()

    transformed_data, ax = task_func(data, n_components)

    assert isinstance(transformed_data, pd.DataFrame)
    assert transformed_data.columns.tolist() == expected_columns
    assert transformed_data.values.tolist() == expected_data.values.tolist()
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_n_components():
    data = np.random.rand(100, 10)
    n_components = -1

    with pytest.raises(ValueError) as exc_info:
        task_func(data, n_components)

    assert str(exc_info.value) == "n_components must be a positive integer"