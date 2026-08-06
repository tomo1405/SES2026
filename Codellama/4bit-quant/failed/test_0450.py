import pytest
from src_0450 import task_func

def test_task_func():
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [10, 20, 30, 40, 50],
        "Feature3": [100, 200, 300, 400, 500],
        "Feature4": [1000, 2000, 3000, 4000, 5000],
        "Feature5": [10000, 20000, 30000, 40000, 50000]
    })

    data_standardized, axes_list = task_func(data)

    assert isinstance(data_standardized, pd.DataFrame)
    assert isinstance(axes_list, list)
    assert len(axes_list) == len(FEATURES)

    for ax in axes_list:
        assert isinstance(ax, plt.Axes)
        assert ax.get_title() == "Histogram of {}".format(ax.get_title())

    for feature in FEATURES:
        assert feature in data_standardized.columns
        assert feature in axes_list[FEATURES.index(feature)].get_title()