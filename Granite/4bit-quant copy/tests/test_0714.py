import os
import re
import pytest

def task_func(log_file_path: str, keywords: list):
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file {log_file_path} does not exist.")
    
    formatted_lines = []
    with open(log_file_path, 'r') as log:
        for line in log:
            for keyword in keywords:
                if keyword in line:
                    parts = re.split(r'\s+', line.strip(), maxsplit=2)
                    if len(parts) == 3:
                        formatted_line = f"{keyword:>{20}} : {parts[1]:>{20}} : {parts[2]:>{20}}"
                        formatted_lines.append(formatted_line)
                    else:
                        # Handle lines that do not conform to expected structure
                        formatted_lines.append(f"Line format unexpected: {line.strip()}")
    return formatted_lines

def test_task_func():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    expected_output = ["keyword1 : part1 : part2", "keyword2 : part3 : part4"]
    
    with open(log_file_path, 'w') as log:
        log.write("line with keyword1 part1 part2\n")
        log.write("line with keyword2 part3 part4\n")
        log.write("line without keyword part5 part6\n")
    
    output = task_func(log_file_path, keywords)
    
    assert output == expected_output, "Output does not match expected output"
    
    os.remove(log_file_path)

if __name__ == "__main__":
    pytest.main()