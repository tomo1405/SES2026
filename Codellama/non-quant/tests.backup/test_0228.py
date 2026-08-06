import pytest
from src_0228 import task_func

def test_task_func():
    # Test case 1: Ensure the function raises an error when the audio file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(L=10, M=10, N=10, audio_file='/path/to/non-existent/file.wav')

    # Test case 2: Ensure the function returns the correct matrix and figure object
    L = 10
    M = 10
    N = 10
    audio_file = 'path/to/audio/file.wav'
    matrix, fig = task_func(L, M, N, audio_file)
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (M, N)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_xlabel() == 'Time'
    assert fig.axes[0].get_ylabel() == 'Log'
    assert fig.axes[0].get_title() == 'Spectrogram'