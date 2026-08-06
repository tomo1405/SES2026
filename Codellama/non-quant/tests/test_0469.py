import pytest
from src_0469 import task_func

def test_task_func():
    file_path = "data.csv"
    columns = ["A", "B", "C"]
    df, ax, croot = task_func(file_path, columns)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert isinstance(croot, np.ndarray)
    assert df.shape == (10, 3)
    assert ax.shape == (10, 3)
    assert croot.shape == (10, 3)
    assert np.allclose(df[columns], np.cbrt(df[columns]))