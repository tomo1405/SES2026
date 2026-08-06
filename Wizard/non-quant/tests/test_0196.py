python
import subprocess
import platform
import time

def task_func(url):
    if platform.system() == 'Darwin':
        cmd = 'open'
    elif platform.system() == 'Windows':
        cmd = 'start'
    else:
        cmd = 'xdg-open'

    # Open webpage in a background process
    process = subprocess.Popen([cmd, url], shell=True)

    # Wait for the process to complete
    while process.poll() is None:
        time.sleep(1)

    return process.returncode

def test_task_func():
    # Test case 1: Open a webpage on macOS
    if platform.system() == 'Darwin':
        url = 'https://www.apple.com/'
        process = subprocess.Popen(['open', url], shell=True)
        while process.poll() is None:
            time.sleep(1)
        assert process.returncode == 0

    # Test case 2: Open a webpage on Windows
    if platform.system() == 'Windows':
        url = 'https://www.microsoft.com/'
        process = subprocess.Popen(['start', url], shell=True)
        while process.poll() is None:
            time.sleep(1)
        assert process.returncode == 0

    # Test case 3: Open a webpage on Linux
    if platform.system() == 'Linux':
        url = 'https://www.linux.org/'
        process = subprocess.Popen(['xdg-open', url], shell=True)
        while process.poll() is None:
            time.sleep(1)
        assert process.returncode == 0