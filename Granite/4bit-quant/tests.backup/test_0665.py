import pytest
from src_0665 import task_func

def test_task_func():
    # Mock sales_data DataFrame
    sales_data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Sales1': [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320],
        'Sales2': [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        'Sales3': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
    }

    # Call the function with the mock data
    ax = task_func(sales_data)

    # Add assertions to test the output
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    assert ax.get_legend().get_texts()[0].get_text() == 'Sales1'
    assert ax.get_legend().get_texts()[1].get_text() == 'Sales2'
    assert ax.get_legend().get_texts()[2].get_text() == 'Sales3'
    assert ax.get_xticks()[0] == 'Jan'
    assert ax.get_xticks()[1] == 'Feb'
    assert ax.get_xticks()[2] == 'Mar'
    assert ax.get_xticks()[3] == 'Apr'
    assert ax.get_xticks()[4] == 'May'
    assert ax.get_xticks()[5] == 'Jun'
    assert ax.get_xticks()[6] == 'Jul'
    assert ax.get_xticks()[7] == 'Aug'
    assert ax.get_xticks()[8] == 'Sep'
    assert ax.get_xticks()[9] == 'Oct'
    assert ax.get_xticks()[10] == 'Nov'
    assert ax.get_xticks()[11] == 'Dec'

if __name__ == "__main__":
    pytest.main()