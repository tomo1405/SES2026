import pandas as pd
import pytest
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    df = pd.read_csv(data_file_path)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col].replace(",", "", regex=True), errors="coerce")
    df = df.dropna(axis=1)
    means = df.mean()
    std_devs = df.std()
    axes = []
    for col in df.columns:
        ax = df[col].hist(bins=50)
        ax.set_title(col)
        axes.append(ax)
    if len(df.columns) > 1:
        anova_results = pd.DataFrame(f_oneway(*[df[col] for col in df.columns if df[col].dtype != 'object']),
                                     index=['F-value', 'P-value'], 
                                     columns=['ANOVA Results'])
    else:
        anova_results = None
    return means, std_devs, axes, anova_results

def test_task_func():
    # Test case 1: Test with a valid CSV file
    data_file_path = "valid_data.csv"
    means, std_devs, axes, anova_results = task_func(data_file_path)
    assert isinstance(means, pd.Series)
    assert isinstance(std_devs, pd.Series)
    assert isinstance(axes, list)
    assert all(isinstance(ax, plt.Axes) for ax in axes)
    assert isinstance(anova_results, pd.DataFrame) or anova_results is None

    # Test case 2: Test with an invalid CSV file
    data_file_path = "invalid_data.csv"
    with pytest.raises(Exception) as excinfo:
        task_func(data_file_path)
    assert "Unable to read CSV file" in str(excinfo.value)

    # Test case 3: Test with a CSV file containing only strings
    data_file_path = "string_data.csv"
    means, std_devs, axes, anova_results = task_func(data_file_path)
    assert isinstance(means, pd.Series)
    assert isinstance(std_devs, pd.Series)
    assert isinstance(axes, list)
    assert all(isinstance(ax, plt.Axes) for ax in axes)
    assert anova_results is None