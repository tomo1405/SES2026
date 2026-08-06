python
import pandas as pd
import numpy as np
import pytest

def task_func(product_dict, product_keys):
    columns = ['Product', 'Quantity', 'Price', 'Profit']
    data = []

    for key in product_keys:
        quantity, price = product_dict[key]
        profit = quantity * price
        data.append([key, quantity, price, profit])

    df = pd.DataFrame(data, columns=columns)

    if not df.empty:
        # Calculate average price and average profit using numpy
        avg_price = np.mean(df['Price'])
        avg_profit = np.mean(df['Profit'])

        # Add average price and average profit as new columns to the dataframe
        df['Average Price'] = avg_price
        df['Average Profit'] = avg_profit

        ax = df.plot(x='Product', y='Profit', kind='bar', legend=False, title="Profit for each product")
        ax.set_ylabel("Profit")
    else:
        ax = None

    return df, ax

def test_task_func():
    # Test case 1: Valid input
    product_dict = {'Product A': (10, 5), 'Product B': (20, 10), 'Product C': (15, 7)}
    product_keys = ['Product A', 'Product B', 'Product C']
    expected_df = pd.DataFrame({'Product': ['Product A', 'Product B', 'Product C'],
                                'Quantity': [10, 20, 15],
                                'Price': [5, 10, 7],
                                'Profit': [50, 200, 125],
                                'Average Price': [5, 10, 7],
                                'Average Profit': [50, 200, 125]})
    expected_ax = None
    actual_df, actual_ax = task_func(product_dict, product_keys)
    assert actual_df.equals(expected_df)
    assert actual_ax == expected_ax

    # Test case 2: Empty dataframe
    product_dict = {}
    product_keys = []
    expected_df = pd.DataFrame(columns=['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])
    expected_ax = None
    actual_df, actual_ax = task_func(product_dict, product_keys)
    assert actual_df.equals(expected_df)
    assert actual_ax == expected_ax

    # Test case 3: Invalid input (non-numeric quantity)
    product_dict = {'Product A': ('10', 5), 'Product B': (20, 10), 'Product C': (15, 7)}
    product_keys = ['Product A', 'Product B', 'Product C']
    with pytest.raises(TypeError):
        task_func(product_dict, product_keys)

    # Test case 4: Invalid input (non-numeric price)
    product_dict = {'Product A': (10, '5'), 'Product B': (20, 10), 'Product C': (15, 7)}
    product_keys = ['Product A', 'Product B', 'Product C']
    with pytest.raises(TypeError):
        task_func(product_dict, product_keys)

    # Test case 5: Invalid input (non-numeric quantity and price)
    product_dict = {'Product A': ('10', '5'), 'Product B': (20, '10'), 'Product C': (15, '7')}
    product_keys = ['Product A', 'Product B', 'Product C']
    with pytest.raises(TypeError):
        task_func(product_dict, product_keys)