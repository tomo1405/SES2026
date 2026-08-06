import pytest
from src_0283 import task_func
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Mocking the necessary components
class MockAxes3D:
    def plot(self, x, y, color=None):
        pass

class MockFigure:
    def __init__(self):
        self.ax = MockAxes3D()
    
    def canvas(self):
        return self.Canvas()

    class Canvas:
        def mpl_connect(self, event, callback):
            pass

@pytest.fixture
def mock_file_path(tmpdir):
    p = tmpdir.mkdir("sub").join("test_image.png")
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(str(p), img)
    return str(p)

@pytest.fixture
def mock_onpick():
    def onpick(event):
        pass
    return onpick

def test_task_func(mock_file_path, mock_onpick, monkeypatch):
    # Mocking the figure creation
    mock_figure = MockFigure()
    monkeypatch.setattr(plt, 'figure', lambda: mock_figure)
    
    # Call the function
    ax = task_func(mock_file_path, mock_onpick)
    
    # Assertions
    assert isinstance(ax, MockAxes3D)
    assert os.path.exists(mock_file_path)

def test_task_func_file_not_found(monkeypatch):
    def mock_exists(path):
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.png", lambda event: None)
    
    assert "No file found at non_existent_file.png" in str(excinfo.value)