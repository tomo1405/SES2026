import pytest
from src_0347 import task_func

def test_task_func_script_exists():
    with pytest.raises(ValueError):
        task_func("non_existent_script.py")

def test_task_func_script_runs_successfully(tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("print('Hello, World!')")
    
    returncode = task_func(str(script_path))
    assert returncode == 0

def test_task_func_script_fails(tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("import sys; sys.exit(1)")
    
    with pytest.raises(subprocess.CalledProcessError):
        task_func(str(script_path))

def test_task_func_no_wait(tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("time.sleep(2); print('Done')")
    
    result = task_func(str(script_path), wait=False)
    assert result is None

def test_task_func_with_args(tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("import sys; print(sys.argv[1])")
    
    returncode = task_func(str(script_path), wait=True, "arg1")
    assert returncode == 0