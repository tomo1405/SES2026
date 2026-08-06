import pytest
from src_0563 import task_func

def test_task_func():
    # Test 1: Invalid filepath type
    with pytest.raises(TypeError):
        task_func(123)

    # Test 2: Invalid filepath
    with pytest.raises(OSError):
        task_func("")

    # Test 3: Valid filepath
    lib = task_func("path/to/file.so")
    assert isinstance(lib, ctypes.CDLL)
    assert lib._name == "file.so"

    # Test 4: System information
    uname = os.uname()
    assert uname.sysname == "Linux"
    assert uname.nodename == "localhost"
    assert uname.release == "5.10.0-10-amd64"
    assert uname.version == "#1 SMP Debian 5.10.60-3+deb10u2 (2021-05-13)"
    assert uname.machine == "x86_64"

    # Test 5: Python version
    python_version = sys.version
    assert python_version == "3.9.5 (default, May  3 2021, 17:31:06) \n[GCC 10.2.1 20210110]"

    # Test 6: PIP version
    pip_version = subprocess.check_output(['pip', '--version'])
    assert pip_version.decode("utf-8") == "pip 21.2.4 from /usr/lib/python3.9/site-packages/pip (python 3.9)"