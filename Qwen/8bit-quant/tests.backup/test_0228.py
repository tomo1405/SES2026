import pytest
from src_0228 import task_func
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

# Mocking dependencies
class MockLibrosa:
    @staticmethod
    def amplitude_to_db(amplitude, ref):
        return amplitude

    @staticmethod
    def stft(matrix):
        return np.abs(matrix)

    @staticmethod
    def display.specshow(D, sr, x_axis, y_axis):
        pass

class MockSoundFile:
    @staticmethod
    def read(file_path):
        return np.random.rand(1000), 44100

class MockMatplotlib:
    @staticmethod
    def colorbar(format):
        pass

    @staticmethod
    def title(title):
        pass

    @staticmethod
    def gcf():
        return "Figure Object"

@pytest.fixture
def mock_dependencies(monkeypatch):
    monkeypatch.setattr(os, 'path.isfile', lambda x: True)
    monkeypatch.setattr(sf, 'read', MockSoundFile.read)
    monkeypatch.setattr(librosa, 'amplitude_to_db', MockLibrosa.amplitude_to_db)
    monkeypatch.setattr(librosa, 'stft', MockLibrosa.stft)
    monkeypatch.setattr(librosa.display, 'specshow', MockLibrosa.display.specshow)
    monkeypatch.setattr(plt, 'colorbar', MockMatplotlib.colorbar)
    monkeypatch.setattr(plt, 'title', MockMatplotlib.title)
    monkeypatch.setattr(plt, 'gcf', MockMatplotlib.gcf)

def test_task_func(mock_dependencies):
    L = np.arange(50)
    M = 5
    N = 10
    audio_file = "test_audio.wav"

    matrix, fig = task_func(L, M, N, audio_file)

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (M, N)
    assert isinstance(fig, str)  # Mocked to return a string representation

def test_task_func_nonexistent_file(mock_dependencies):
    L = np.arange(50)
    M = 5
    N = 10
    audio_file = "nonexistent_audio.wav"

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(L, M, N, audio_file)

    assert str(excinfo.value) == "nonexistent_audio.wav does not exist."