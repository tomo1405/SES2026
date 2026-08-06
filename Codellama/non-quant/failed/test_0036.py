import pytest
from src_0036 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5]})
    target_values = [1, 3, 4]
    expected_df = pd.DataFrame({'A': [1, 0, 3, 4, 0], 'B': [1, 0, 3, 4, 0]})
    expected_ax = plt.gca()
    sns.kdeplot(expected_df['A'], label='A', warn_singular=False)
    sns.kdeplot(expected_df['B'], label='B', warn_singular=False)
    plt.legend()
    expected_ax.set_xlabel('Values')
    expected_ax.set_ylabel('Density')
    expected_ax.set_title('KDE Plot of A and B')
    result_df, result_ax = task_func(df, target_values)
    assert result_df.equals(expected_df)
    assert result_ax.get_xlabel() == expected_ax.get_xlabel()
    assert result_ax.get_ylabel() == expected_ax.get_ylabel()
    assert result_ax.get_title() == expected_ax.get_title()
    assert result_ax.get_legend().get_texts() == expected_ax.get_legend().get_texts()
    assert result_ax.get_legend().get_lines() == expected_ax.get_legend().get_lines()