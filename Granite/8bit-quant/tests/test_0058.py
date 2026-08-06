import pytest
from src_0058 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    title = "Heatmap of Correlation Matrix"
    corr, ax = task_func(csv_file_path, title)
    assert isinstance(corr, pd.DataFrame), "Correlation matrix is not a DataFrame"
    assert isinstance(ax, plt.Axes), " axes object is not an instance of plt.Axes"
    assert ax.get_title() == title, "Title does not match"