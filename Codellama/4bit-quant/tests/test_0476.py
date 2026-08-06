from datetime import datetime

import matplotlib
import pandas as pd
import pytest
from src_0476 import task_func


def test_task_func():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}

    ax = task_func(data, date_format, country, country_codes)

    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Date Distribution'
    assert ax.get_ylabel() == 'Frequency'
    assert len(ax.get_xticks()) == 3
    assert ax.get_xticks()[0] == datetime.strptime('2022-01-01', date_format).date()
    assert ax.get_xticks()[1] == datetime.strptime('2022-01-02', date_format).date()
    assert ax.get_xticks()[2] == datetime.strptime('2022-01-03', date_format).date()
    assert ax.get_yticks()[0] == 1
    assert ax.get_yticks()[1] == 1
    assert ax.get_yticks()[2] == 1

def test_task_func_invalid_input():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}

    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)