import os
import re
import pytest
from src_0714 import task_func

def test_task_func():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    expected_output = ["keyword1 : part1 : part2", "keyword2 : part3 : part4"]
    
    if not os.path.exists(log_file_path):
        with pytest.raises(FileNotFoundError):
            task_func(log_file_path, keywords)
    else:
        with open(log_file_path, 'r') as log:
            lines = log.readlines()
            for line in lines:
                for keyword in keywords:
                    if keyword in line:
                        parts = re.split(r'\s+', line.strip(), maxsplit=2)
                        if len(parts) == 3:
                            formatted_line = f"{keyword:>{20}} : {parts[1]:>{20}} : {parts[2]:>{20}}"
                            assert formatted_line in expected_output
                        else:
                            # Handle lines that do not conform to expected structure
                            assert f"Line format unexpected: {line.strip()}" in expected_output