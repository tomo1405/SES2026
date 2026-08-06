import pytest
from src_0665 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'Month': [1, 2, 3, 4, 5],
        'Sales1': [100, 150, 120, 130, 140],
        'Sales2': [110, 120, 130, 140, 150]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    fig, ax = plt.subplots()
    result = task_func(sample_data)
    assert result == ax
    plt.close()