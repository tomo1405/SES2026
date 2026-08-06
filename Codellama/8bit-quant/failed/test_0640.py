import pytest
from src_0640 import task_func

def test_task_func():
    num_samples = 100
    num_features = 5
    df, ax = task_func(num_samples, num_features)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert len(df) == num_samples
    assert len(df.columns) == num_features
    assert len(df.index) == num_samples
    assert df.columns.tolist() == ['Feature' + str(i) for i in range(1, num_features + 1)]
    assert df.index.tolist() == ['Sample' + str(i) for i in range(1, num_samples + 1)]
    assert np.allclose(df.values, np.random.rand(num_samples, num_features))
    assert np.allclose(corr_matrix.values, df.corr().values)