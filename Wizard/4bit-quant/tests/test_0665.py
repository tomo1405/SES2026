python
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import pytest

from src_0665 import task_func

@pytest.fixture
def sales_data():
    data = {'Month': [1, 2, 3, 4, 5],
            'Product A': [100, 120, 110, 140, 130],
            'Product B': [50, 60, 55, 70, 65]}
    return pd.DataFrame(data)

def test_task_func(sales_data):
    fig, ax = plt.subplots()
    for label in sales_data.columns[1:]:  # Skipping 'Month' column
        monthly_sales = sales_data[label]
        std_dev = statistics.stdev(monthly_sales)

        ax.plot(sales_data['Month'], monthly_sales, label=label)
        ax.fill_between(sales_data['Month'],
                        monthly_sales - std_dev,
                        monthly_sales + std_dev,
                        alpha=0.2)

    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly Sales Trends with Standard Deviation')
    ax.legend()

    # Set x-ticks to be explicit months from the DataFrame
    ax.set_xticks(sales_data['Month'])

    assert ax == task_func(sales_data)