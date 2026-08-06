import pytest
from src_0094 import task_func

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    expected_columns = ['PC1', 'PC2']

    result, ax = task_func(data, n_components)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
    assert result.columns.tolist() == expected_columns
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'