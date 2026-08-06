import pytest
from src_0640 import task_func

def test_task_func():
    num_samples = 100
    num_features = 5
    df, ax = task_func(num_samples, num_features)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert df.shape == (num_samples, num_features)
    assert df.index.name == 'Sample'
    assert df.columns.name == 'Feature'
    assert np.allclose(df.values, np.random.rand(num_samples, num_features))
    assert np.allclose(corr_matrix, df.corr())
    assert ax.get_xlabel() == 'Feature'
    assert ax.get_ylabel() == 'Sample'
    assert ax.get_title() == 'Correlation Matrix'