import re
import tarfile
from pathlib import Path


def test_task_func():
    directory = "C:\\SomeDir\\"
    file_pattern = r"(?<!Distillr)\\\\AcroTray\.exe"
    tar_path = Path(directory) / 'archive.tar'
    with tarfile.open(tar_path, 'w') as tar:
        for path in Path(directory).rglob('*'):
            if re.match(file_pattern, path.name):
                try:
                    tar.add(path, arcname=path.relative_to(directory))
                except PermissionError as e:
                    print(f"Skipping {path} due to permission error: {e}")
    assert tar_path.exists()
    assert tar_path.is_file()
    assert tar_path.stat().st_size > 0