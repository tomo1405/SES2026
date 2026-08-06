import pytest
from src_0363 import task_func

def test_task_func():
    # Test that the function raises an error when the original file does not exist
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.xlsx")

    # Test that the function raises an error when the sheet name is invalid
    with pytest.raises(ValueError):
        task_func("test.xlsx", sheet_name="invalid_sheet")

    # Test that the function returns the correct data when the original file exists and the sheet name is valid
    original_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    original_df.to_excel("test.xlsx", index=False)
    new_df = task_func("test.xlsx", sheet_name="Sheet1")
    assert new_df.equals(original_df)

    # Test that the function writes the correct data to the new Excel file
    new_df = pd.read_excel("new_test.xlsx")
    assert new_df.equals(original_df)