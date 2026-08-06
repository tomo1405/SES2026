from src_0952 import task_func


def test_task_func_output():
    mystrings = ["Laptop", "T-Shirt", "Blender", "Novel", "Toy Car"]
    n_products = 5
    seed_value = 0

    result_df = task_func(mystrings, n_products, seed_value)

    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == n_products, "The number of products does not match the expected value."

    # Check if the DataFrame has the correct columns
    expected_columns = ['Product Name', 'Category', 'Price']
    assert all(column in result_df.columns for column in expected_columns), "The DataFrame does not contain the expected columns."

    # Check if the 'Product Name' values are valid
    valid_product_names = [name.replace(' ', '_') for name in mystrings]
    assert all(name in valid_product_names for name in result_df['Product Name']), "The 'Product Name' contains invalid values."

    # Check if the 'Category' values are valid
    assert all(category in CATEGORIES for category in result_df['Category']), "The 'Category' contains invalid values."

    # Check if the 'Price' values are within the expected range
    assert all(30 <= price <= 70 for price in result_df['Price']), "The 'Price' values are out of the expected range."

def test_task_func_with_zero_products():
    mystrings = ["Laptop", "T-Shirt", "Blender", "Novel", "Toy Car"]
    n_products = 0
    seed_value = 0

    result_df = task_func(mystrings, n_products, seed_value)

    # Check if the DataFrame is empty
    assert result_df.empty, "The DataFrame should be empty when n_products is 0."

def test_task_func_with_single_product():
    mystrings = ["Laptop"]
    n_products = 1
    seed_value = 0

    result_df = task_func(mystrings, n_products, seed_value)

    # Check if the DataFrame has exactly one row
    assert len(result_df) == 1, "The DataFrame should have exactly one product when n_products is 1."

    # Check if the 'Product Name' is valid
    valid_product_name = mystrings[0].replace(' ', '_')
    assert result_df['Product Name'].iloc[0] == valid_product_name, "The 'Product Name' is invalid."

    # Check if the 'Category' is valid
    assert result_df['Category'].iloc[0] in CATEGORIES, "The 'Category' is invalid."

    # Check if the 'Price' is within the expected range
    assert 30 <= result_df['Price'].iloc[0] <= 70, "The 'Price' is out of the expected range."