import pytest
from src_0058 import task_func

def test_task_func():
    csv_file_path = 'path/to/csv/file.csv'
    title = 'Correlation Heatmap'
    corr, ax = task_func(csv_file_path, title)
    assert isinstance(corr, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert corr.shape == (10, 10)
    assert ax.get_title() == title