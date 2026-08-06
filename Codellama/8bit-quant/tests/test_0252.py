import pytest
from src_0252 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = pd.DataFrame({'Job': ['A', 'B', 'C', 'D', 'E']})
    result = task_func(data)
    assert isinstance(result, plt.Figure)
    assert result.axes[0].get_title() == 'Job Distribution'
    assert result.axes[0].get_xlabel() == 'Job'
    assert result.axes[0].get_ylabel() == 'Count'
    assert len(result.axes[0].get_legend().get_texts()) == 5
    assert result.axes[0].get_legend().get_texts()[0].get_text() == 'A'
    assert result.axes[0].get_legend().get_texts()[1].get_text() == 'B'
    assert result.axes[0].get_legend().get_texts()[2].get_text() == 'C'
    assert result.axes[0].get_legend().get_texts()[3].get_text() == 'D'
    assert result.axes[0].get_legend().get_texts()[4].get_text() == 'E'
    assert result.axes[0].get_legend().get_texts()[0].get_color() == 'red'
    assert result.axes[0].get_legend().get_texts()[1].get_color() == 'blue'
    assert result.axes[0].get_legend().get_texts()[2].get_color() == 'green'
    assert result.axes[0].get_legend().get_texts()[3].get_color() == 'yellow'
    assert result.axes[0].get_legend().get_texts()[4].get_color() == 'orange'