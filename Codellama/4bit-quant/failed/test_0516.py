import pytest
from src_0516 import task_func

def test_task_func():
    # Test with valid input
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, heatmap = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(heatmap, sns.heatmap)
    assert df.columns.tolist() == ["A", "B", "C", "D", "E"]
    assert len(df) == 2
    assert len(df.columns) == 5
    assert len(heatmap.get_children()) == 1

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func([])
    with pytest.raises(ValueError):
        task_func([[1, 2, 3, 4], [5, 6, 7, 8]])