import pytest
from src_0008 import task_func

def test_task_func():
    # Create a temporary CSV file for testing
    csv_content = """product,quantity
apple,10
banana,20
orange,15
banana,10"""

    with open('test_sales_data.csv', 'w') as f:
        f.write(csv_content)

    # Test the function
    result = task_func('test_sales_data.csv')

    # Clean up the temporary file
    import os
    os.remove('test_sales_data.csv')

    # Assert the result
    assert result == 'banana'

def test_task_func_with_tie():
    # Create a temporary CSV file for testing with a tie
    csv_content = """product,quantity
apple,10
banana,10
orange,10"""

    with open('test_sales_data_tie.csv', 'w') as f:
        f.write(csv_content)

    # Test the function
    result = task_func('test_sales_data_tie.csv')

    # Clean up the temporary file
    import os
    os.remove('test_sales_data_tie.csv')

    # Assert the result (it can be any of the tied products)
    assert result in ['apple', 'banana', 'orange']

def test_task_func_empty_file():
    # Create a temporary empty CSV file for testing
    with open('test_sales_data_empty.csv', 'w') as f:
        pass

    # Test the function
    with pytest.raises(ValueError):
        task_func('test_sales_data_empty.csv')

    # Clean up the temporary file
    import os
    os.remove('test_sales_data_empty.csv')