python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(csv_file_path: str, title: str):
    data = pd.read_csv(csv_file_path)
    corr = data.corr().round(2)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True)
    plt.title(title)
    return corr, plt.gca()

def test_task_func():
    # Test case 1: Test with valid input
    csv_file_path = "data.csv"
    title = "Correlation Matrix"
    corr, ax = task_func(csv_file_path, title)
    assert isinstance(corr, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == title
    
    # Test case 2: Test with invalid input
    with pytest.raises(TypeError):
        task_func(123, "Correlation Matrix")