python
import pytest
from src_0094 import task_func

def test_task_func():
    data = np.random.rand(100, 5)
    transformed_data, ax = task_func(data, n_components=2)
    assert isinstance(transformed_data, pd.DataFrame)
    assert transformed_data.shape == (100, 2)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'
    assert ax.get_title() == 'PCA transformed data'