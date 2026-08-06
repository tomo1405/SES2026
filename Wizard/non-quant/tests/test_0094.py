python
import pytest
from src_0094 import task_func

def test_task_func():
    data = np.random.rand(100, 5)
    n_components = 2
    
    result, ax = task_func(data, n_components)
    
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (100, 2)
    assert all(col in result.columns for col in ['PC1', 'PC2'])
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'