import pandas as pd
from src_0066 import task_func


def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'C', 'col3': 'D'},
        {'col1': 'B', 'col2': 'C', 'col3': 'D'},
    ]
    expected_analyzed_df = pd.DataFrame(
        {'col1': ['A', 'A', 'B'], 'col2': ['B', 'C', 'C'], 'col3': [2, 2, 1]},
        columns=COLUMNS
    )
    expected_ax = plt.subplots()[1]
    expected_ax.plot(expected_analyzed_df[COLUMNS[:-1]].astype(str).agg('-'.join, axis=1), expected_analyzed_df[COLUMNS[-1]])
    expected_ax.set_xlabel('-'.join(COLUMNS[:-1]))
    expected_ax.set_ylabel(COLUMNS[-1])

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert ax.get_ylim() == expected_ax.get_ylim()
    assert ax.get_xticks() == expected_ax.get_xticks()
    assert ax.get_yticks() == expected_ax.get_yticks()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_xaxis().get_major_formatter().format_data(ax.get_xdata()) == expected_ax.get_xaxis().get_major_formatter().format_data(expected_ax.get_xdata())
    assert ax.get_yaxis().get_major_formatter().format_data(ax.get_ydata()) == expected_ax.get_yaxis().get_major_formatter().format_data(expected_ax.get_ydata())