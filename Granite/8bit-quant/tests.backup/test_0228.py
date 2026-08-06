import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
from src_0228 import task_func

def test_task_func():
    L = np.random.rand(100, 100)
    M, N = 10, 10
    audio_file = "test_audio.wav"
    matrix, fig = task_func(L, M, N, audio_file)
    assert matrix.shape == (M, N)
    assert isinstance(fig, plt.Figure)

def test_file_not_found_error():
    L = np.random.rand(100, 100)
    M, N = 10, 10
    audio_file = "nonexistent_audio.wav"
    with pytest.raises(FileNotFoundError):
        task_func(L, M, N, audio_file)