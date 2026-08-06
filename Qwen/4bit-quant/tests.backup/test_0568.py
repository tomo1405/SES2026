import pytest
from src_0568 import task_func
import io
import sys

# Mocking plt.show() to capture output instead of displaying it
@pytest.fixture
def mock_plt_show(monkeypatch):
    mock = io.StringIO()
    monkeypatch.setattr(sys.stdout, "write", mock.write)
    return mock

def test_task_func(mock_plt_show):
    input_data = "1-2-3-4-5"
    result = task_func(input_data)
    
    # Check if the function returns an Axes object
    assert isinstance(result, plt.Axes), "The function should return a matplotlib Axes object."
    
    # Since plt.show() is mocked, we can't directly check the plot.
    # Instead, we can check if the function runs without errors and returns the correct type.
    # Additional checks would require more complex mocking or capturing the plot output.