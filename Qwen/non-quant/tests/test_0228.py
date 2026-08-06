import pytest
from src_0228 import task_func
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

# Mocking the necessary functions and classes
class MockSoundFile:
    def read(self, file_path):
        return np.random.rand(1000), 44100

class MockLibrosa:
    def stft(self, data):
        return np.random.rand(100, 50)

    def amplitude_to_db(self, S, ref=np.max):
        return S

class MockMatplotlib:
    def specshow(self, D, sr, x_axis, y_axis):
        pass

    def display(self):
        return self

    def colorbar(self, format):
        pass

    def title(self, title):
        pass

    def gcf(self):
        return self

@pytest.fixture
def mock_soundfile(monkeypatch):
    monkeypatch.setattr(sf, 'read', MockSoundFile().read)

@pytest.fixture
def mock_librosa(monkeypatch):
    monkeypatch.setattr(librosa, 'stft', MockLibrosa().stft)
    monkeypatch.setattr(librosa, 'amplitude_to_db', MockLibrosa().amplitude_to_db)
    monkeypatch.setattr(librosa.display, 'specshow', MockMatplotlib().specshow)

@pytest.fixture
def mock_matplotlib(monkeypatch):
    monkeypatch.setattr(plt, 'gcf', MockMatplotlib().gcf)
    monkeypatch.setattr(plt, 'colorbar', MockMatplotlib().colorbar)
    monkeypatch.setattr(plt, 'title', MockMatplotlib().title)

@pytest.fixture
def mock_os(monkeypatch):
    def mock_isfile(path):
        return True
    monkeypatch.setattr(os, 'isfile', mock_isfile)

def test_task_func(mock_soundfile, mock_librosa, mock_matplotlib, mock_os):
    L = np.arange(100)
    M = 10
    N = 10
    audio_file = "test_audio.wav"

    matrix, fig = task_func(L, M, N, audio_file)

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (M, N)
    assert isinstance(fig, MockMatplotlib)

def test_task_func_file_not_found(mock_os):
    L = np.arange(100)
    M = 10
    N = 10
    audio_file = "non_existent_audio.wav"

    with pytest.raises(FileNotFoundError):
        task_func(L, M, N, audio_file)