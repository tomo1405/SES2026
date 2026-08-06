import pytest
from src_0048 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    # Capture the output of the heatmap
    old_stdout = io.StringIO()
    plt.rcParams['figure.autolayout'] = True
    with io.capture_output() as captured:
        transformed_df, heatmap = task_func(sample_df)
    
    # Check if the dataframe is transformed correctly
    assert not transformed_df.isnull().values.any(), "DataFrame contains NaN values after transformation"
    assert transformed_df.shape == sample_df.shape, "DataFrame shape changed after transformation"
    
    # Check if the heatmap is created
    assert isinstance(heatmap, sns.axisgrid.heatmap, "Heatmap is not created")
    
    # Check if the plot is drawn
    assert captured.stdout.strip() == "", "Plot was not drawn without showing"
    
    # Check if the data is scaled correctly
    scaler = StandardScaler()
    expected_scaled_data = scaler.fit_transform(sample_df.fillna(sample_df.mean()))
    assert np.allclose(transformed_df.values, expected_scaled_data), "Data scaling is incorrect"