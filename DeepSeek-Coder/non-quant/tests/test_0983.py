import pytest
from src_0983 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Create a sample DataFrame for testing
    data = np.random.randn(100)
    df = pd.DataFrame({'column': data})

    # Call the function with the sample DataFrame
    result = task_func(df=df, column='column')

    # Add assertions to verify the output
    assert result is not None
    assert isinstance(result, plt.Axes)
    assert plt.gcf().get_axes()