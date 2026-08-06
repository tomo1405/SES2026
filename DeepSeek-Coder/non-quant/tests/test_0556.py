import pytest
from src_0556 import task_func
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

@pytest.fixture
def sample_data():
    np.random.seed(0)
    a = np.random.rand(10)
    b = a * 2 + np.random.normal(0, 0.1, 10)
    return a, b

def test_task_func(sample_data):
    a, b = sample_data
    correlation, _ = stats.pearsonr(a, b)
    df = pd.DataFrame({'A': a, 'B': b})

    plt.scatter(df['A'], df['B'])
    plt.plot(np.unique(df['A']), np.poly1d(np.polyfit(df['A'], df['B'], 1))(np.unique(df['A'])), color='red')
    plt.show()
    assert correlation, plt.gca()