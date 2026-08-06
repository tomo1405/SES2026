import numpy as np
from src_0043 import task_func


def test_task_func():
    data_matrix = [[1, 2], [3, 4], [5, 6]]
    n_components = 2
    df, ax = task_func(data_matrix, n_components)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape[1] == n_components
    assert df.columns.tolist() == [f"Component {i+1}" for i in range(n_components)]
    assert df["Mean"].tolist() == [np.mean(data_matrix, axis=1)]
    assert np.allclose(np.cumsum(pca.explained_variance_ratio_), ax.lines[0].get_ydata())
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"