import pytest
from src_0074 import task_func

def test_task_func():
    db_file = "test_db.db"
    df, ax = task_func(db_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert "sum" in df.columns
    assert "mean" in df.columns
    assert "var" in df.columns
    assert df["sum"].dtype == np.float64
    assert df["mean"].dtype == np.float64
    assert df["var"].dtype == np.float64
    assert ax.get_xlabel() == "EmailData"
    assert ax.get_ylabel() == "Sum, Mean, Variance"
    assert ax.get_title() == "Email Data Summary"