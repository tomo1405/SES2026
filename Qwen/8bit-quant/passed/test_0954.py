import pytest
from src_0954 import task_func
import os
import shutil
import numpy as np

@pytest.fixture
def temp_folder(tmpdir):
    return tmpdir.mkdir("test_plots")

def test_task_func_with_seed(temp_folder):
    mystrings = ["test1", "test2", "test1"]
    seed = 42
    result = task_func(mystrings, str(temp_folder), seed=seed)
    assert len(result) == 2
    assert "test1.png" in result
    assert "test2.png" in result

    # Check that the files are actually saved
    assert os.path.exists(os.path.join(str(temp_folder), "test1.png"))
    assert os.path.exists(os.path.join(str(temp_folder), "test2.png"))

    # Check that the files are not identical
    with open(os.path.join(str(temp_folder), "test1.png"), "rb") as f1:
        content1 = f1.read()
    with open(os.path.join(str(temp_folder), "test2.png"), "rb") as f2:
        content2 = f2.read()
    assert content1 != content2

def test_task_func_without_seed(temp_folder):
    mystrings = ["test3", "test4"]
    result = task_func(mystrings, str(temp_folder))
    assert len(result) == 2
    assert "test3.png" in result
    assert "test4.png" in result

    # Check that the files are actually saved
    assert os.path.exists(os.path.join(str(temp_folder), "test3.png"))
    assert os.path.exists(os.path.join(str(temp_folder), "test4.png"))

def test_task_func_duplicate_names(temp_folder):
    mystrings = ["test5", "test5", "test5"]
    result = task_func(mystrings, str(temp_folder))
    assert len(result) == 1
    assert "test5.png" in result

    # Check that only one file is saved
    assert os.path.exists(os.path.join(str(temp_folder), "test5.png"))

def test_task_func_nonexistent_folder(temp_folder):
    non_existent_path = os.path.join(str(temp_folder), "non_existent")
    mystrings = ["test6"]
    result = task_func(mystrings, non_existent_path)
    assert len(result) == 1
    assert "test6.png" in result

    # Check that the folder was created and the file is saved
    assert os.path.exists(non_existent_path)
    assert os.path.exists(os.path.join(non_existent_path, "test6.png"))

def teardown_function():
    # Clean up any temporary files or folders created during tests
    shutil.rmtree("test_plots", ignore_errors=True)