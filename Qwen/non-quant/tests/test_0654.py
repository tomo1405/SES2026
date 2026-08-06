import pytest
from src_0654 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@pytest.fixture
def sample_dataframe():
    data = {
        'A': ['1', '2', '332', '4'],
        'B': ['332', '5', '6', '7'],
        'C': ['8', '9', '10', '332']
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe, monkeypatch):
    # Mock the plt.show() call to prevent the plot from displaying
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Call the function with the sample dataframe
    mask, ax = task_func(sample_dataframe, target_value='332')

    # Check if the mask is a DataFrame of the same shape as the input dataframe
    assert isinstance(mask, pd.DataFrame)
    assert mask.shape == sample_dataframe.shape

    # Check if the mask contains only boolean values
    assert mask.dtypes.apply(lambda x: pd.api.types.is_bool_dtype(x)).all()

    # Check if the heatmap was created correctly
    assert isinstance(ax, sns.axisgrid.AxesGrid)

    # Check if the mask values are correct
    expected_mask = pd.DataFrame({
        'A': [False, False, True, False],
        'B': [True, False, False, False],
        'C': [False, False, False, True]
    })
    assert mask.equals(expected_mask)