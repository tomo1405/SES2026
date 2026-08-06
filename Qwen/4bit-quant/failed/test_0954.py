import pytest
from src_0954 import task_func
import os
import tempfile
import numpy as np

def test_task_func():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define test inputs
        mystrings = ["test plot", "another plot", "test plot"]
        seed = 42

        # Call the function
        result = task_func(mystrings, temp_dir, seed=seed)

        # Check that the correct number of unique plots were saved
        assert len(result) == 2, "The number of unique plots should be 2"

        # Check that the plots have the correct names
        expected_files = ["test_plot.png", "another_plot.png"]
        assert set(result) == set(expected_files), "The plot files do not match the expected names"

        # Check that the files exist in the directory
        for file_name in expected_files:
            assert os.path.exists(os.path.join(temp_dir, file_name)), f"File {file_name} does not exist in {temp_dir}"

        # Check that the random data is reproducible with the same seed
        np.random.seed(seed)
        data = np.random.rand(10)
        assert np.allclose(data, [0.37454012, 0.95071431, 0.73199394, 0.59865848, 0.15601864,
                                   0.15599452, 0.05808366, 0.71009146, 0.42318462, 0.68166838]), \
            "Random data does not match the expected values with the given seed"

def test_task_func_no_seed():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define test inputs
        mystrings = ["no seed plot"]

        # Call the function without a seed
        result = task_func(mystrings, temp_dir)

        # Check that the correct number of unique plots were saved
        assert len(result) == 1, "The number of unique plots should be 1"

        # Check that the plots have the correct names
        expected_files = ["no_seed_plot.png"]
        assert set(result) == set(expected_files), "The plot files do not match the expected names"

        # Check that the files exist in the directory
        for file_name in expected_files:
            assert os.path.exists(os.path.join(temp_dir, file_name)), f"File {file_name} does not exist in {temp_dir}"

def test_task_func_empty_strings():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define test inputs
        mystrings = ["", "   ", "non-empty string"]

        # Call the function
        result = task_func(mystrings, temp_dir)

        # Check that the correct number of unique plots were saved
        assert len(result) == 1, "The number of unique plots should be 1"

        # Check that the plots have the correct names
        expected_files = ["non_empty_string.png"]
        assert set(result) == set(expected_files), "The plot files do not match the expected names"

        # Check that the files exist in the directory
        for file_name in expected_files:
            assert os.path.exists(os.path.join(temp_dir, file_name)), f"File {file_name} does not exist in {temp_dir}"