python
import pytest
from src_0503 import task_func

def test_task_func():
    # Test with default arguments
    ax, df = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 7
    assert df.shape[1] == 3
    assert df.columns.tolist() == ["Date", "Activity", "Duration"]
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Duration"].dtype == "int64"
    assert df["Activity"].dtype == "object"
    assert ax.axes.shape == (1, 1)
    assert ax.axes[0, 0].get_xlabel() == "Date"
    assert ax.axes[0, 0].get_ylabel() == "Duration"
    assert ax.axes[0, 0].get_title() == "Duration by Activity"
    assert ax.get_legend().texts[0].get_text() == "Running"
    assert ax.get_legend().texts[1].get_text() == "Swimming"
    assert ax.get_legend().texts[2].get_text() == "Cycling"
    assert ax.get_legend().texts[3].get_text() == "Yoga"
    assert ax.get_legend().texts[4].get_text() == "Weight Training"

    # Test with custom arguments
    ax, df = task_func(days_in_past=30, random_seed=42)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 30
    assert df.shape[1] == 3
    assert df.columns.tolist() == ["Date", "Activity", "Duration"]
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Duration"].dtype == "int64"
    assert df["Activity"].dtype == "object"
    assert ax.axes.shape == (1, 1)
    assert ax.axes[0, 0].get_xlabel() == "Date"
    assert ax.axes[0, 0].get_ylabel() == "Duration"
    assert ax.axes[0, 0].get_title() == "Duration by Activity"
    assert ax.get_legend().texts[0].get_text() == "Running"
    assert ax.get_legend().texts[1].get_text() == "Swimming"
    assert ax.get_legend().texts[2].get_text() == "Cycling"
    assert ax.get_legend().texts[3].get_text() == "Yoga"
    assert ax.get_legend().texts[4].get_text() == "Weight Training"

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(days_in_past=0)
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)