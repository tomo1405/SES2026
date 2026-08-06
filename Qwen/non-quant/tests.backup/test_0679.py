import pytest
from src_0679 import task_func
import pandas as pd
import os
import shutil
import tempfile

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result_df = task_func(temp_dir)
        assert result_df.empty

def test_task_func_single_json_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        data = {"key": "value"}
        json_file_path = os.path.join(temp_dir, "test.json")
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        result_df = task_func(temp_dir)
        expected_df = pd.DataFrame([{"key": "value", "source": "test.json"}])
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

def test_task_func_multiple_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        data1 = {"key1": "value1"}
        data2 = [{"key2": "value2"}, {"key3": "value3"}]
        
        json_file_path1 = os.path.join(temp_dir, "test1.json")
        json_file_path2 = os.path.join(temp_dir, "test2.json")
        
        with open(json_file_path1, 'w') as json_file1:
            json.dump(data1, json_file1)
        
        with open(json_file_path2, 'w') as json_file2:
            json.dump(data2, json_file2)

        result_df = task_func(temp_dir)
        expected_df = pd.DataFrame([
            {"key1": "value1", "source": "test1.json"},
            {"key2": "value2", "source": "test2.json"},
            {"key3": "value3", "source": "test2.json"}
        ])
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

def test_task_func_non_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        text_file_path = os.path.join(temp_dir, "test.txt")
        with open(text_file_path, 'w') as text_file:
            text_file.write("This is a test.")

        result_df = task_func(temp_dir)
        assert result_df.empty

def test_task_func_processed_directory_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        processed_path = os.path.join(temp_dir, 'processed')
        os.makedirs(processed_path)

        data = {"key": "value"}
        json_file_path = os.path.join(temp_dir, "test.json")
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        result_df = task_func(temp_dir)
        expected_df = pd.DataFrame([{"key": "value", "source": "test.json"}])
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

def test_task_func_move_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        data = {"key": "value"}
        json_file_path = os.path.join(temp_dir, "test.json")
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        task_func(temp_dir)
        processed_path = os.path.join(temp_dir, 'processed')
        assert os.path.exists(os.path.join(processed_path, "test.json"))
        assert not os.path.exists(json_file_path)