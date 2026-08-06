import pytest
from src_0665 import task_func

def test_task_func():
    # Mock sales_data DataFrame
    sales_data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Product A': [100, 120, 150, 180, 200, 220, 250, 230, 200, 180, 150, 120],
        'Product B': [80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 110],
        'Product C': [50, 60, 70, 80, 90, 100, 110, 120, 110, 100, 90, 80]
    }

    # Call the function and store the returned ax object
    ax = task_func(sales_data)

    # Assert that the returned ax object has the expected properties
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    assert ax.get_legend_handles()  # Check if the legend is displayed

    # Assert that the x-ticks are set to the explicit months from the DataFrame
    assert ax.get_xticks().tolist() == sales_data['Month']

if __name__ == '__main__':
    pytest.main()