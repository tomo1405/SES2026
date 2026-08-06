from src_0172 import task_func


def test_task_func():
    # Test with a simple dictionary
    vegetable_dict = {'A': 'Carrot', 'B': 'Potato'}
    df = task_func(vegetable_dict, seed=42)
    
    # Check that the DataFrame has the correct columns
    assert list(df.columns) == ['Count', 'Percentage']
    
    # Check that the DataFrame has the correct index
    assert list(df.index) == ['Carrot', 'Potato']
    
    # Check that the counts are within the expected range
    assert all(1 <= count <= 10 for count in df['Count'])
    
    # Check that the percentages sum to 100
    assert round(df['Percentage'].sum(), 5) == 100.0

def test_task_func_with_empty_dict():
    # Test with an empty dictionary
    vegetable_dict = {}
    df = task_func(vegetable_dict, seed=42)
    
    # Check that the DataFrame is empty
    assert df.empty

def test_task_func_with_all_vegetables():
    # Test with a dictionary containing all vegetables
    vegetable_dict = {str(i): veg for i, veg in enumerate(VEGETABLES)}
    df = task_func(vegetable_dict, seed=42)
    
    # Check that the DataFrame has the correct columns
    assert list(df.columns) == ['Count', 'Percentage']
    
    # Check that the DataFrame has the correct index
    assert list(df.index) == VEGETABLES
    
    # Check that the counts are within the expected range
    assert all(1 <= count <= 10 for count in df['Count'])
    
    # Check that the percentages sum to 100
    assert round(df['Percentage'].sum(), 5) == 100.0

def test_task_func_with_duplicate_values():
    # Test with a dictionary containing duplicate values
    vegetable_dict = {'A': 'Carrot', 'B': 'Carrot'}
    df = task_func(vegetable_dict, seed=42)
    
    # Check that the DataFrame has the correct columns
    assert list(df.columns) == ['Count', 'Percentage']
    
    # Check that the DataFrame has the correct index
    assert list(df.index) == ['Carrot']
    
    # Check that the counts are within the expected range
    assert all(1 <= count <= 10 for count in df['Count'])
    
    # Check that the percentages sum to 100
    assert round(df['Percentage'].sum(), 5) == 100.0