import pytest
from src_0654 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mocking the plt and sns show functions to avoid displaying plots during tests
plt.show = lambda: None
sns.heatmap = lambda *args, **kwargs: plt.gca()

@pytest.fixture
def sample_dataframe():
    data = {
        'A': ['1', '2', '332', '4'],
        'B': ['5', '332', '7', '8'],
        'C': ['9', '10', '11', '332']
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    target_value = '332'
    mask, ax = task_func(sample_dataframe, target_value)
    
    # Check if the mask is a DataFrame of the same shape as the input dataframe
    assert isinstance(mask, pd.DataFrame)
    assert mask.shape == sample_dataframe.shape
    
    # Check if the mask contains True where the target value is present
    expected_mask = sample_dataframe.applymap(lambda x: x == target_value)
    assert mask.equals(expected_mask)
    
    # Check if the ax object is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)