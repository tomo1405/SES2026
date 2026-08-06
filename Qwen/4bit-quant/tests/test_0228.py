import pytest
from src_0228 import task_func
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

# Mocking dependencies for testing
class MockSF:
    @staticmethod
    def read(file):
        return np.array([0.1, 0.2, 0.3]), 44100

class MockLibrosa:
    @staticmethod
    def amplitude_to_db(S, ref=np.max):
        return S

class MockMatplotlib:
    @staticmethod
    def display_specshow(D, sr, x_axis, y_axis):
        pass

    @staticmethod
    def colorbar(mappable, format):
        pass

    @staticmethod
    def title(title):
        pass

    @staticmethod
    def gcf():
        return "MockFigure"

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    monkeypatch.setattr(sf, 'read', MockSF.read)
    monkeypatch.setattr(librosa, 'amplitude_to_db', MockLibrosa.amplitude_to_db)
    monkeypatch.setattr(librosa.display, 'specshow', MockMatplotlib.display_specshow)
    monkeypatch.setattr(plt, 'colorbar', MockMatplotlib.colorbar)
    monkeypatch.setattr(plt, 'title', MockMatplotlib.title)
    monkeypatch.setattr(plt, 'gcf', MockMatplotlib.gcf)

def test_task_func_exists():
    assert callable(task_func)

def test_task_func_raises_file_not_found_error(tmp_path):
    non_existent_file = tmp_path / "non_existent.wav"
    with pytest.raises(FileNotFoundError):
        task_func(1, 1, 1, str(non_existent_file))

def test_task_func_correct_output(tmp_path):
    # Create a temporary audio file
    audio_file = tmp_path / "test_audio.wav"
    sf.write(str(audio_file), np.random.rand(44100), 44100)

    L = np.array([1, 2, 3, 4])
    M, N = 2, 2

    matrix, fig = task_func(L, M, N, str(audio_file))

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (M, N)
    assert fig == "MockFigure"