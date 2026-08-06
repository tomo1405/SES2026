import pytest
from src_0684 import task_func

# Mocking the yaml module to simulate file operations
class MockYaml:
    def __init__(self, content):
        self.content = content

    def safe_load(self, file):
        return self.content

    def safe_dump(self, data, file):
        self.content = data

@pytest.fixture
def mock_yaml(monkeypatch):
    yaml_content = {'angle': 0}
    mock = MockYaml(yaml_content)
    monkeypatch.setattr('yaml', mock)
    return mock

def test_task_func_updates_value(mock_yaml, tmp_path):
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml.dump({'angle': 0}))

    result = task_func(str(yaml_file), 'angle')

    assert math.isclose(result['angle'], 1.0)

def test_task_func_no_change(mock_yaml, tmp_path):
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml.dump({'not_angle': 0}))

    result = task_func(str(yaml_file), 'angle')

    assert result == {'not_angle': 0}

def test_task_func_nonexistent_key(mock_yaml, tmp_path):
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml.dump({'angle': 0}))

    result = task_func(str(yaml_file), 'nonexistent_key')

    assert result == {'angle': 0}