import pytest
from src_0361 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import tempfile

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="No file found at .*"):
        task_func("non_existent_file.xlsx", "Sheet1")

def test_task_func_sheet_not_found():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        try:
            with pytest.raises(ValueError, match="Error reading sheet: .*"):
                task_func(temp_file.name, "NonExistentSheet")
        finally:
            os.remove(temp_file.name)

def test_task_func_valid_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        try:
            df.to_excel(temp_file.name, index=False, sheet_name='Sheet1')
            result, fig = task_func(temp_file.name, 'Sheet1')
            expected_result = {
                'A': {'mean': 2.0, 'std': np.sqrt(2/3)},
                'B': {'mean': 5.0, 'std': np.sqrt(2/3)}
            }
            assert result == expected_result
            assert isinstance(fig, plt.Figure)
        finally:
            os.remove(temp_file.name)