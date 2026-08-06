import pytest
from src_0030 import task_func
from sklearn.preprocessing import StandardScaler
import numpy as np
import base64

def test_task_func():
    # Test case 1: Test with a 2D array of shape (3, 2)
    data = np.array([[1, 2], [3, 4], [5, 6]])
    expected_output = "dHVuZHJhLm1hdHJpeC5pc2tlcmlhbC5TaW1wbGVTY2FsZXIoKVsnc3RhdGljYWxpemVkX2RhdGEnXShbWzMsIDRdKVswXVsxXVswXSA9IDAuMDAzNjQxNjM2MzMzMzMzMzM="
    output = task_func(data)
    assert output == expected_output, "Test case 1 failed"

    # Test case 2: Test with a 1D array of shape (5,)
    data = np.array([1, 2, 3, 4, 5])
    expected_output = "dHVuZHJhLm1hdHJpeC5pc2tlcmlhbC5TaW1wbGVTY2FsZXIoKVsnc3RhdGljYWxpemVkX2RhdGEnXShbMSwgMiwgMywgNCwgNV0pWydzdHJpbmcgZG9jdW1lbnQnXSA9ICcnXFxuJCRbJG51bWJlclN0cmluZygpXShbc3RhdGljYWxpemVkX2RhdGEgMSwgc3RhdGljYWxpemVkX2RhdGEgMiwg..."
    output = task_func(data)
    assert output == expected_output, "Test case 2 failed"

    # Test case 3: Test with an empty array
    data = np.array([])
    expected_output = ""
    output = task_func(data)
    assert output == expected_output, "Test case 3 failed"

if __name__ == "__main__":
    pytest.main()