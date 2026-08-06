import pytest
from src_0363 import task_func

def test_task_func_valid_input():
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"

    # Create a sample Excel file
    with pd.ExcelWriter(original_file_location) as writer:
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Call the function with valid input
    new_df = task_func(original_file_location, new_file_location, sheet_name)

    # Check that the new Excel file was created
    assert os.path.exists(new_file_location)

    # Check that the data was written correctly
    expected_df = pd.read_excel(new_file_location)
    pd.testing.assert_frame_equal(new_df, expected_df)

def test_task_func_invalid_input():
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    sheet_name = "Sheet1"

    # Call the function with invalid input
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location, new_file_location, sheet_name)

    # Check that the new Excel file was not created
    assert not os.path.exists(new_file_location)