import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0038 import task_func


@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3, 4],
        'feature2': [5, 6, 7, 8],
        'target': [0, 1, 0, 1]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    model, ax = task_func(sample_df, 'target')
    
    # Check if the model is an instance of RandomForestClassifier
    assert isinstance(model, RandomForestClassifier)
    
    # Check if the feature importance series has the correct length
    assert len(model.feature_importances_) == 2
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot title is set correctly
    assert ax.get_title() == "Visualizing Important Features"
    
    # Check if the x and y labels are set correctly
    assert ax.get_xlabel() == "Feature Importance Score"
    assert ax.get_ylabel() == "Features"

# Run the tests
if __name__ == "__main__":
    pytest.main()