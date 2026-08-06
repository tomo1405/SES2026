import pytest
from src_0068 import task_func
import pandas as pd
import os
import re

# Mocking os and os.path modules for testing
class MockOs:
    def listdir(self, path):
        return ['EMP1.txt', 'EMP2.txt', 'NOEMP3.txt']

    def path(self):
        class MockPath:
            def getsize(self, path):
                return 1024  # Mock size of each file

        return MockPath()

os = MockOs()

def test_task_func():
    dir_path = '/mock/path'
    expected_df = pd.DataFrame({
        'File': ['EMP1.txt', 'EMP2.txt'],
        'Size': [1024, 1024]
    })
    result_df = task_func(dir_path)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_no_matching_files():
    dir_path = '/mock/path'
    os.listdir = lambda path: ['NOEMP1.txt', 'NOEMP2.txt']
    expected_df = pd.DataFrame(columns=['File', 'Size'])
    result_df = task_func(dir_path)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_directory():
    dir_path = '/mock/path'
    os.listdir = lambda path: []
    expected_df = pd.DataFrame(columns=['File', 'Size'])
    result_df = task_func(dir_path)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_custom_pattern():
    dir_path = '/mock/path'
    os.listdir = lambda path: ['ABC1.txt', 'XYZ2.txt']
    expected_df = pd.DataFrame({
        'File': ['ABC1.txt', 'XYZ2.txt'],
        'Size': [1024, 1024]
    })
    result_df = task_func(dir_path, pattern='^[A-Z]{3}')
    pd.testing.assert_frame_equal(result_df, expected_df)