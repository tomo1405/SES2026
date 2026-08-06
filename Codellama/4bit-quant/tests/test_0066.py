import pandas as pd
from src_0066 import task_func


def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'B', 'col3': 'E'},
        {'col1': 'A', 'col2': 'B', 'col3': 'F'},
        {'col1': 'A', 'col2': 'B', 'col3': 'G'},
        {'col1': 'A', 'col2': 'B', 'col3': 'H'},
        {'col1': 'A', 'col2': 'B', 'col3': 'I'},
        {'col1': 'A', 'col2': 'B', 'col3': 'J'},
        {'col1': 'A', 'col2': 'B', 'col3': 'K'},
        {'col1': 'A', 'col2': 'B', 'col3': 'L'},
        {'col1': 'A', 'col2': 'B', 'col3': 'M'},
        {'col1': 'A', 'col2': 'B', 'col3': 'N'},
        {'col1': 'A', 'col2': 'B', 'col3': 'O'},
        {'col1': 'A', 'col2': 'B', 'col3': 'P'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Q'},
        {'col1': 'A', 'col2': 'B', 'col3': 'R'},
        {'col1': 'A', 'col2': 'B', 'col3': 'S'},
        {'col1': 'A', 'col2': 'B', 'col3': 'T'},
        {'col1': 'A', 'col2': 'B', 'col3': 'U'},
        {'col1': 'A', 'col2': 'B', 'col3': 'V'},
        {'col1': 'A', 'col2': 'B', 'col3': 'W'},
        {'col1': 'A', 'col2': 'B', 'col3': 'X'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Y'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Z'}
    ]
    expected_analyzed_df = pd.DataFrame(data, columns=COLUMNS)
    expected_analyzed_df = expected_analyzed_df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    expected_ax = plt.subplots()
    expected_ax.plot(expected_analyzed_df[COLUMNS[:-1]].astype(str).agg('-'.join, axis=1), expected_analyzed_df[COLUMNS[-1]])
    expected_ax.set_xlabel('-'.join(COLUMNS[:-1]))
    expected_ax.set_ylabel(COLUMNS[-1])

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xaxis().get_ticklabels() == expected_ax.get_xaxis().get_ticklabels()
    assert ax.get_yaxis().get_ticklabels() == expected_ax.get_yaxis().get_ticklabels()
    assert ax.get_legend().get_title().get_text() == expected_ax.get_legend().get_title().get_text()
    assert ax.get_legend().get_texts() == expected_ax.get_legend().get_texts()