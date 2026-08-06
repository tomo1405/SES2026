import pytest
from src_0073 import task_func
import pandas as pd
import os
import numpy as np
import ast

def test_task_func():
    # Test case 1: Basic functionality
    directory = "test_directory"
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "file1.csv"), "w") as f:
        f.write("email,list\nuser1,1,2,3\nuser2,4,5,6")
    with open(os.path.join(directory, "file2.csv"), "w") as f:
        f.write("email,list\nuser3,7,8,9\nuser4,10,11,12")
    
    result = task_func(directory)
    assert isinstance(result, tuple)
    assert isinstance(result[0], pd.DataFrame)
    assert len(result[0]) > 0
    assert "sum" in result[0].columns
    assert "mean" in result[0].columns
    assert "median" in result[0].columns
    os.rmdir(directory)

    # Add more test cases as needed

pytest.main()