import pytest
from src_0083 import task_func

def test_task_func():
    app = task_func('secret_key', 'template_folder')
    assert app.config['SECRET_KEY'] == 'secret_key'
    assert app.template_folder == 'template_folder'
    # Add more tests as needed

if __name__ == '__main__':
    pytest.main()