import pandas as pd
from src_0665 import task_func


def test_task_func():
    sales_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [100, 120, 150, 100, 100, 150]
    })

    ax = task_func(sales_data)

    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    assert len(ax.get_xticks()) == 6
    assert len(ax.get_yticks()) == 6
    assert len(ax.get_lines()) == 6
    assert len(ax.get_legend().get_texts()) == 6

    for i in range(6):
        assert ax.get_xticks()[i] == sales_data['Month'][i]
        assert ax.get_yticks()[i] == sales_data['Sales'][i]
        assert ax.get_lines()[i].get_label() == sales_data.columns[i+1]
        assert ax.get_legend().get_texts()[i].get_text() == sales_data.columns[i+1]