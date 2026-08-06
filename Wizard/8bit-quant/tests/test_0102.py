python
import pytest
from src_0102 import task_func

def test_task_func():
    # Test case 1: Default data_url and seed
    ax = task_func()
    assert isinstance(ax, sns.axisgrid.JointGrid)

    # Test case 2: Custom data_url and seed
    ax = task_func(data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", seed=123)
    assert isinstance(ax, sns.axisgrid.JointGrid)

    # Test case 3: Invalid data_url
    with pytest.raises(ValueError):
        task_func(data_url="invalid_url")

    # Test case 4: Invalid seed
    with pytest.raises(ValueError):
        task_func(seed="invalid_seed")