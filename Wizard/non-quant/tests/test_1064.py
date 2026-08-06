python
import pytest
from src_1064 import task_func

def test_task_func():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Explained Variance Ratio of Principal Components"
    assert ax.get_xticks() == [0]
    assert ax.get_xticklabels() == ["PC1"]
    assert ax.get_yticks() == []
    assert ax.get_yticklabels() == []
    assert ax.get_xlabel() == "Principal Component"
    assert ax.get_ylabel() == "Explained Variance Ratio"
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xlim() == (-0.5, 0.5)
    assert ax.get_lines()[0].get_data() == ([0], [0.5])
    assert ax.get_lines()[0].get_color() == "black"
    assert ax.get_lines()[0].get_marker() == "o"
    assert ax.get_lines()[0].get_markersize() == 10
    assert ax.get_lines()[0].get_linestyle() == "None"
    assert ax.get_lines()[1].get_data() == ([0], [0.5])
    assert ax.get_lines()[1].get_color() == "black"
    assert ax.get_lines()[1].get_marker() == "o"
    assert ax.get_lines()[1].get_markersize() == 10
    assert ax.get_lines()[1].get_linestyle() == "None"
    assert ax.get_legend().get_texts()[0].get_text() == "PC1"
    assert ax.get_legend().get_texts()[0].get_color() == "black"
    assert ax.get_legend().get_texts()[0].get_fontsize() == "medium"
    assert ax.get_legend().get_lines()[0].get_color() == "black"
    assert ax.get_legend().get_lines()[0].get_linestyle() == "None"
    assert ax.get_legend().get_lines()[0].get_linewidth() == 1.0
    assert ax.get_legend().get_frame().get_facecolor() == "white"
    assert ax.get_legend().get_frame().get_edgecolor() == "black"
    assert ax.get_legend().get_frame().get_linewidth() == 0.5
    plt.close()