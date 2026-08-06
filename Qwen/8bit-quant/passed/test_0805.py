import pytest
from src_0805 import task_func

def test_task_func_valid_input(tmp_path):
    # Arrange
    metrics = {'metric1': 10, 'metric2': 20}
    filename = 'test_log.txt'
    log_dir = tmp_path / 'logs'
    log_dir.mkdir()

    # Act
    result = task_func(metrics, filename, log_dir=str(log_dir))

    # Assert
    assert result is True
    log_file = log_dir / filename
    assert log_file.exists()
    with open(log_file, 'r') as f:
        lines = f.readlines()
    assert len(lines) == 4  # timestamp + 2 metrics + newline

def test_task_func_invalid_metrics_type():
    # Arrange
    metrics = [1, 2, 3]
    filename = 'test_log.txt'

    # Act & Assert
    with pytest.raises(ValueError, match="Metrics must be a dictionary"):
        task_func(metrics, filename)

def test_task_func_invalid_filename_type():
    # Arrange
    metrics = {'metric1': 10}
    filename = 123

    # Act & Assert
    with pytest.raises(ValueError, match="Filename must be a string"):
        task_func(metrics, filename)

def test_task_func_directory_creation(tmp_path):
    # Arrange
    metrics = {'metric1': 10}
    filename = 'test_log.txt'
    log_dir = tmp_path / 'non_existent_logs'

    # Act
    result = task_func(metrics, filename, log_dir=str(log_dir))

    # Assert
    assert result is True
    assert log_dir.exists()
    log_file = log_dir / filename
    assert log_file.exists()

def test_task_func_file_write_error(tmp_path, monkeypatch):
    # Arrange
    metrics = {'metric1': 10}
    filename = 'test_log.txt'
    log_dir = tmp_path / 'logs'
    log_dir.mkdir()

    def mock_open(*args, **kwargs):
        raise IOError("Mocked I/O error")

    monkeypatch.setattr('builtins.open', mock_open)

    # Act
    result = task_func(metrics, filename, log_dir=str(log_dir))

    # Assert
    assert result is False