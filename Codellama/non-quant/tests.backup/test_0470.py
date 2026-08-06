import pytest
from src_0470 import task_func

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(["A", "B", "C", "D", "E"])

def test_task_func_valid_input():
    student_grades = ["A", "B", "C", "D", "F"]
    report_df, ax = task_func(student_grades)
    assert isinstance(report_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert report_df.shape == (5, 1)
    assert report_df.index.name == "Grade"
    assert report_df.columns.tolist() == ["Count"]
    assert report_df.values.tolist() == [[1], [1], [1], [1], [1]]
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"
    assert ax.get_title() == "Grade Distribution"