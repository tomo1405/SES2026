import pytest
from src_0491 import task_func

def test_task_func():
    s = "<xml>...</xml>"
    file_path = "output.json"
    expected_output = {"key": "value"}

    # Mock the expected behavior of the target function
    def mock_xmltodict_parse(s):
        return expected_output

    # Monkey patch the target function with the mock
    with pytest. MonkeyPatch.context() as mp:
        mp.setattr(task_func, "xmltodict.parse", mock_xmltodict_parse)
        actual_output = task_func(s, file_path)

    assert actual_output == expected_output
    assert "w" in open.call_args[0]
    assert open.call_args[0][0] == file_path
    assert json.dumps(expected_output, indent=4) in open.call_args[0][1]