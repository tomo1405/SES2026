import pytest
from src_0665 import task_func

@pytest.fixture
def sales_data():
    return pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Sales': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
    })

def test_task_func(sales_data):
    ax = task_func(sales_data)
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    assert len(ax.get_xticks()) == 12
    assert len(ax.get_yticks()) == 12
    assert ax.get_legend().get_text() == 'Sales'