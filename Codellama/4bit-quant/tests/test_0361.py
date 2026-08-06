import pytest
from src_0361 import task_func

def test_task_func():
    file_location = "test_data.xlsx"
    sheet_name = "Sheet1"
    result, fig = task_func(file_location, sheet_name)
    assert isinstance(result, dict)
    assert isinstance(fig, matplotlib.figure.Figure)
    assert "mean" in result
    assert "std" in result
    assert result["mean"] == pytest.approx(np.mean(df[column]))
    assert result["std"] == pytest.approx(np.std(df[column]))
    assert fig.axes[0].get_title() == "Mean and Standard Deviation"
    assert fig.axes[0].get_xlabel() == "Columns"
    assert fig.axes[0].get_ylabel() == "Values"