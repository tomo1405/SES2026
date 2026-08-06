python
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
import pytest

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):

    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns.")

    color_cycle = cycle('bgrcmk')
    fig, ax = plt.subplots(figsize=(10, 6))

    for group in groups:
        group_df = df[df['group'] == group].copy()
        group_df['date'] = group_df['date'].apply(lambda x: x.toordinal())
        ax.scatter(group_df['date'], group_df['value'], color=next(color_cycle))

    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('Scatterplot of Values for Each Group Over Time')

    return ax

def test_task_func():
    df = pd.DataFrame({'group': ['A', 'B', 'C', 'D', 'E'],
                       'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-01', '2021-01-02'],
                       'value': [1, 2, 3, 4, 5]})

    ax = task_func(df)

    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Scatterplot of Values for Each Group Over Time'

    assert len(ax.collections) == 5
    assert ax.collections[0].get_offsets().shape == (2, 2)
    assert ax.collections[0].get_facecolors().shape == (4, 4)
    assert ax.collections[0].get_edgecolors().shape == (4, 4)
    assert ax.collections[0].get_sizes().shape == (1,)
    assert ax.collections[0].get_linewidths().shape == (1,)
    assert ax.collections[0].get_alpha().shape == (1,)
    assert ax.collections[0].get_cmap() is None
    assert ax.collections[0].get_norm() is None
    assert ax.collections[0].get_path_effects() is None
    assert ax.collections[0].get_joinstyle() == 'round'
    assert ax.collections[0].get_capstyle() == 'round'
    assert ax.collections[0].get_sketch_params() == (None, None, 0.0)
    assert ax.collections[0].get_snap() is None
    assert ax.collections[0].get_urls() is None
    assert ax.collections[0].get_offset_position() == 'data'
    assert ax.collections[0].get_zorder() == 1

    assert ax.collections[1].get_offsets().shape == (2, 2)
    assert ax.collections[1].get_facecolors().shape == (4, 4)
    assert ax.collections[1].get_edgecolors().shape == (4, 4)
    assert ax.collections[1].get_sizes().shape == (1,)
    assert ax.collections[1].get_linewidths().shape == (1,)
    assert ax.collections[1].get_alpha().shape == (1,)
    assert ax.collections[1].get_cmap() is None
    assert ax.collections[1].get_norm() is None
    assert ax.collections[1].get_path_effects() is None
    assert ax.collections[1].get_joinstyle() == 'round'
    assert ax.collections[1].get_capstyle() == 'round'
    assert ax.collections[1].get_sketch_params() == (None, None, 0.0)
    assert ax.collections[1].get_snap() is None
    assert ax.collections[1].get_urls() is None
    assert ax.collections[1].get_offset_position() == 'data'
    assert ax.collections[1].get_zorder() == 1

    assert ax.collections[2].get_offsets().shape == (2, 2)
    assert ax.collections[2].get_facecolors().shape == (4, 4)
    assert ax.collections[2].get_edgecolors().shape == (4, 4)
    assert ax.collections[2].get_sizes().shape == (1,)
    assert ax.collections[2].get_linewidths().shape == (1,)
    assert ax.collections[2].get_alpha().shape == (1,)
    assert ax.collections[2].get_cmap() is None
    assert ax.collections[2].get_norm() is None
    assert ax.collections[2].get_path_effects() is None
    assert ax.collections[2].get_joinstyle() == 'round'
    assert ax.collections[2].get_capstyle() == 'round'
    assert ax.collections[2].get_sketch_params() == (None, None, 0.0)
    assert ax.collections[2].get_snap() is None
    assert ax.collections[2].get_urls() is None
    assert ax.collections[2].get_offset_position() == 'data'
    assert ax.collections[2].get_zorder() == 1

    assert ax.collections[3].get_offsets().shape == (2, 2)
    assert ax.collections[3].get_facecolors().shape == (4, 4)
    assert ax.collections[3].get_edgecolors().shape == (4, 4)
    assert ax.collections[3].get_sizes().shape == (1,)
    assert ax.collections[3].get_linewidths().shape == (1,)
    assert ax.collections[3].get_alpha().shape == (1,)
    assert ax.collections[3].get_cmap() is None
    assert ax.collections[3].get_norm() is None
    assert ax.collections[3].get_path_effects() is None
    assert ax.collections[3].get_joinstyle() == 'round'
    assert ax.collections[3].get_capstyle() == 'round'
    assert ax.collections[3].get_sketch_params() == (None, None, 0.0)
    assert ax.collections[3].get_snap() is None
    assert ax.collections[3].get_urls() is None
    assert ax.collections[3].get_offset_position() == 'data'
    assert ax.collections[3].get_zorder() == 1

    assert ax.collections[4].get_offsets().shape == (2, 2)
    assert ax.collections[4].get_facecolors().shape == (4, 4)
    assert ax.collections[4].get_edgecolors().shape == (4, 4)
    assert ax.collections[4].get_sizes().shape == (1,)
    assert ax.collections[4].get_linewidths().shape == (1,)
    assert ax.collections[4].get_alpha().shape == (1,)
    assert ax.collections[4].get_cmap() is None
    assert ax.collections[4].get_norm() is None
    assert ax.collections[4].get_path_effects() is None
    assert ax.collections[4].get_joinstyle() == 'round'
    assert ax.collections[4].get_capstyle() == 'round'
    assert ax.collections[4].get_sketch_params() == (None, None, 0.0)
    assert ax.collections[4].get_snap() is None
    assert ax.collections[4].get_urls() is None
    assert ax.collections[4].get_offset_position() == 'data'
    assert ax.collections[4].get_zorder() == 1