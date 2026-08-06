from src_0605 import task_func


def test_task_func_valid_file():
    filepath = 'test_file.cpp'
    with open(filepath, 'w') as f:
        f.write('int main() { return 0; }')
    task_func(filepath)
    assert 'Successfully compiled' in caplog.text

def test_task_func_invalid_file():
    filepath = 'test_file.cpp'
    with open(filepath, 'w') as f:
        f.write('int main() { return 1; }')
    task_func(filepath)
    assert 'Failed to compile' in caplog.text

def test_task_func_invalid_compiler():
    filepath = 'test_file.cpp'
    with open(filepath, 'w') as f:
        f.write('int main() { return 0; }')
    task_func(filepath)
    assert 'Compiler not found or file does not exist' in caplog.text