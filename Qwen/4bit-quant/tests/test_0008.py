import pytest
from src_0008 import task_func

# Mocking the file reading process using pytest-mock
@pytest.fixture
def mock_csv_file(mocker):
    # Create a mock for the open function to simulate file reading
    mock_open = mocker.mock_open(read_data="Product,Quantity\nWidget,10\nGadget,20\nWidget,15")
    mocker.patch('builtins.open', mock_open)
    return mock_open

def test_task_func(mock_csv_file):
    # Define the path to the CSV file
    csv_file_path = 'sales_data.csv'
    
    # Call the function with the mocked CSV file
    result = task_func(csv_file_path)
    
    # Assert that the top selling product is correctly identified
    assert result == 'Widget'

def test_task_func_with_tie(mock_csv_file):
    # Modify the mock data to create a tie in sales
    mock_csv_file.return_value.read_data = "Product,Quantity\nWidget,10\nGadget,20\nTool,20"
    
    # Call the function with the updated mocked CSV file
    result = task_func(csv_file_path)
    
    # Assert that the first product in alphabetical order is returned in case of a tie
    assert result == 'Gadget'  # Assuming 'Gadget' comes before 'Tool' alphabetically

def test_task_func_empty_file(mock_csv_file):
    # Clear the mock data to simulate an empty file
    mock_csv_file.return_value.read_data = ""
    
    # Call the function with the empty mocked CSV file
    result = task_func(csv_file_path)
    
    # Assert that the function returns None when there is no data
    assert result is None

def test_task_func_single_entry(mock_csv_file):
    # Modify the mock data to have only one entry
    mock_csv_file.return_value.read_data = "Product,Quantity\nWidget,10"
    
    # Call the function with the single entry mocked CSV file
    result = task_func(csv_file_path)
    
    # Assert that the single product is returned
    assert result == 'Widget'