from src_0628 import task_func


def test_task_func():
    products_list = ['Product 1', 'Product 2', 'Product 3']
    sales_df = task_func(products_list)

    assert sales_df.shape == (len(products_list), 14)
    assert sales_df.columns.tolist() == ['Product', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6', 'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12', 'Average Sales']
    assert sales_df['Product'].tolist() == products_list
    assert sales_df['Average Sales'].tolist() == [mean(sales_df[f'Month {i+1}'].tolist()) for i in range(12)]