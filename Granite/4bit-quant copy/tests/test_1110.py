import os
from nltk import word_tokenize
def task_func(file_path='File.txt'):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))

    return tokens
import pytest

def test_task_func():
    test_cases = [
        ("File.txt", ["This", "is", "a", "test", "sentence"]),
        ("AnotherFile.txt", ["This", "is", "another", "test", "sentence"]),
    ]

    for file_path, expected_output in test_cases:
        with open(file_path, "w") as file:
            file.write("This is a test sentence.\n")
            file.write("This is another test sentence.\n")

        actual_output = task_func(file_path)
        assert actual_output == expected_output, f"Failed for file_path='{file_path}'"

        os.remove(file_path)

if __name__ == "__main__":
    pytest.main()