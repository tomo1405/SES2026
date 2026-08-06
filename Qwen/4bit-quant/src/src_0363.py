import pandas as pd
import os
def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"No file found at {original_file_location}")

    # Read data from the original Excel file
    try:
        original_df = pd.read_excel(original_file_location, sheet_name=sheet_name)
    except ValueError as e:
        raise ValueError(f"Error reading sheet: {e}")

    # Write data to a new Excel file
    original_df.to_excel(new_file_location, index=False)

    # Read and return data from the new Excel file
    new_df = pd.read_excel(new_file_location)
    return new_df