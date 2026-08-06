import pytest
from src_0954 import task_func
import os
import shutil
import numpy as np

@pytest.fixture
def temp_folder(tmpdir):
    return str(tmpdir.mkdir("test_folder"))

def test_task_func_with_no_strings(temp_folder):
    result = task_func([], temp_folder)
    assert result == []

def test_task_func_with_single_string(temp_folder):
    result = task_func(["test"], temp_folder)
    assert result == ["test.png"]
    assert os.path.exists(os.path.join(temp_folder, "test.png"))

def test_task_func_with_multiple_strings(temp_folder):
    result = task_func(["test1", "test2", "test3"], temp_folder)
    assert result == ["test1.png", "test2.png", "test3.png"]
    for name in result:
        assert os.path.exists(os.path.join(temp_folder, name))

def test_task_func_with_duplicate_strings(temp_folder):
    result = task_func(["test1", "test2", "test1"], temp_folder)
    assert result == ["test1.png", "test2.png"]
    for name in result:
        assert os.path.exists(os.path.join(temp_folder, name))

def test_task_func_with_seed(temp_folder):
    np.random.seed(0)
    result1 = task_func(["test"], temp_folder, seed=0)
    np.random.seed(0)
    result2 = task_func(["test"], temp_folder, seed=0)
    assert result1 == result2
    for name in result1:
        img1 = plt.imread(os.path.join(temp_folder, name))
        img2 = plt.imread(os.path.join(temp_folder, name))
        assert np.array_equal(img1, img2)

def test_task_func_with_nonexistent_folder(temp_folder):
    non_existent_path = os.path.join(temp_folder, "non_existent")
    result = task_func(["test"], non_existent_path)
    assert result == ["test.png"]
    assert os.path.exists(os.path.join(non_existent_path, "test.png"))

def teardown_function():
    # Clean up any temporary files created during tests
    for root, dirs, files in os.walk(temp_folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))