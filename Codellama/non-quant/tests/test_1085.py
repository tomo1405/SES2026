import pytest
from src_1085 import task_func

def test_task_func():
    data_file_path = "data.csv"
    means, std_devs, axes, anova_results = task_func(data_file_path)

    # Test that the output is a tuple
    assert isinstance(means, tuple)
    assert isinstance(std_devs, tuple)
    assert isinstance(axes, list)
    assert isinstance(anova_results, pd.DataFrame)

    # Test that the output has the correct shape
    assert len(means) == len(df.columns)
    assert len(std_devs) == len(df.columns)
    assert len(axes) == len(df.columns)
    assert len(anova_results) == len(df.columns)

    # Test that the output is correct
    assert all(means[i] == df[col].mean() for i, col in enumerate(df.columns))
    assert all(std_devs[i] == df[col].std() for i, col in enumerate(df.columns))
    assert all(axes[i].get_title() == col for i, col in enumerate(df.columns))
    assert all(anova_results.index == ['F-value', 'P-value'])
    assert all(anova_results.columns == ['ANOVA Results'])
    assert all(anova_results.values == f_oneway(*[df[col] for col in df.columns if df[col].dtype != 'object']))