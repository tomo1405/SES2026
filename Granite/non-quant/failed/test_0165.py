import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pytest

def task_func(num_labels=5, data_range=(0, 1)):
    np.random.seed(0)
    columns = [f'Label{i + 1}' for i in range(num_labels)]
    data = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)), columns=columns)

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

def test_task_func():
    # Test case 1: Default arguments
    fig = task_func()
    assert isinstance(fig, plt.Figure)

    # Test case 2: Custom arguments
    fig = task_func(num_labels=10, data_range=(0, 100))
    assert isinstance(fig, plt.Figure)

    # Test case 3: Invalid argument type
    with pytest.raises(TypeError):
        fig = task_func(num_labels=' five', data_range=(0, 100))

    # Test case 4: Invalid argument value
    with pytest.raises(ValueError):
        fig = task_func(num_labels=0, data_range=(0, 100))