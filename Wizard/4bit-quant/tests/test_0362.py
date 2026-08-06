python
import pandas as pd
import logging
import pytest

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        logging.info('Reading the Excel file.')
        # Reading the Excel file
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)

        logging.info('Converting to CSV.')
        # Converting to CSV
        df.to_csv(csv_file_location, index=False)

        # Calculating the sum of each column
        column_sum = df.sum(numeric_only=True)
    except FileNotFoundError:
        logging.error(f"Excel file not found at {excel_file_location}")
        raise FileNotFoundError(f"Excel file not found at {excel_file_location}")
    except ValueError as e:
        logging.error(f"Error in processing Excel file: {e}")
        raise ValueError(f"Error in processing Excel file: {e}")

    return column_sum.to_dict()

def test_task_func():
    # Test case 1: Valid sheet name
    assert task_func('Sheet1') == {'A': 100, 'B': 200, 'C': 300}

    # Test case 2: Invalid sheet name
    with pytest.raises(ValueError):
        task_func('InvalidSheetName')

    # Test case 3: Excel file not found
    with pytest.raises(FileNotFoundError):
        task_func('Sheet1', excel_file_location='invalid_file.xlsx')

    # Test case 4: Error in processing Excel file
    with pytest.raises(ValueError):
        task_func('Sheet1', excel_file_location='test_error.xlsx')