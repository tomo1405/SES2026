import pytest
from src_0973 import task_func

@pytest.mark.parametrize("path, expected", [
    ("example/path/with/slashes", ["example", "path", "with", "slashes"]),
    ("another/example/path", ["another", "example", "path"]),
    ("single/component", ["single", "component"]),
    ("path/with/leading/slash/", ["path", "with", "leading", "slash"]),
    ("path/with/trailing/slash/", ["path", "with", "trailing", "slash"]),
    ("path/with/empty/component//", ["path", "with", "empty", "component"]),
    ("path/with/invalid/characters:<>", ["path", "with", "invalid", "characters"]),
])
def test_task_func(path, expected):
    assert task_func(path) == expected