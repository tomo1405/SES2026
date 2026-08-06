import pathlib
import os
import pytest

def task_func(path: str, delimiter: str = os.path.sep) -> list:

    if not path:
        return []

    path = path.replace("\\", "/")

    path_obj = pathlib.Path(path)

    invalid_chars = set('<>:"|?*')
    if any(
        set(str(component)).intersection(invalid_chars) for component in path_obj.parts
    ):
        return []

    return [
        component
        for component in path_obj.parts
        if component and component != delimiter
    ]

def test_task_func():
    assert task_func("") == []
    assert task_func("C:/Users/John/Documents") == ["C:", "Users", "John", "Documents"]
    assert task_func("C:\\Users\\John\\Documents") == ["C:", "Users", "John", "Documents"]
    assert task_func("/home/john/documents") == ["home", "john", "documents"]
    assert task_func("/home/john/documents/", "/") == ["home", "john", "documents"]
    assert task_func("/home/john/documents/my file.txt") == ["home", "john", "documents", "my file.txt"]
    assert task_func("/home/john/documents/my file.txt", "/") == ["home", "john", "documents", "my file.txt"]
    assert task_func("/home/john/documents/my file.txt", "\\") == ["home", "john", "documents", "my", "file.txt"]
    assert task_func("C:/Users/John/Documents/my file.txt", "\\") == ["C:", "Users", "John", "Documents", "my", "file.txt"]
    assert task_func("C:\\Users\\John\\Documents\\my file.txt", "\\") == ["C:", "Users", "John", "Documents", "my", "file.txt"]
    assert task_func("C:\\Users\\John\\Documents\\my file.txt", "/") == ["C:", "Users", "John", "Documents", "my file.txt"]
    assert task_func("C:/Users/John/Documents/my file.txt", "/") == ["C:", "Users", "John", "Documents", "my file.txt"]
    assert task_func("C:/Users/John/Documents/my<file.txt", "/") == ["C:", "Users", "John", "Documents", "my<file.txt"]
    assert task_func("C:/Users/John/Documents/my>file.txt", "/") == ["C:", "Users", "John", "Documents", "my>file.txt"]
    assert task_func("C:/Users/John/Documents/my|file.txt", "/") == ["C:", "Users", "John", "Documents", "my|file.txt"]
    assert task_func("C:/Users/John/Documents/my:file.txt", "/") == ["C:", "Users", "John", "Documents", "my:file.txt"]
    assert task_func("C:/Users/John/Documents/my\"file.txt", "/") == ["C:", "Users", "John", "Documents", "my\"file.txt"]
    assert task_func("C:/Users/John/Documents/my*file.txt", "/") == ["C:", "Users", "John", "Documents", "my*file.txt"]
    assert task_func("C:/Users/John/Documents/my?file.txt", "/") == ["C:", "Users", "John", "Documents", "my?file.txt"]