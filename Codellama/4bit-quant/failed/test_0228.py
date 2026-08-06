import pytest
from src_0228 import task_func

def test_task_func():
    # Test case 1: Ensure the audio file exists
    with pytest.raises(FileNotFoundError):
        task_func(L=10, M=10, N=10, audio_file='/path/to/audio/file.wav')

    # Test case 2: Ensure the matrix is generated correctly
    matrix, fig = task_func(L=10, M=10, N=10, audio_file='/path/to/audio/file.wav')
    assert matrix.shape == (10, 10)

    # Test case 3: Ensure the spectrogram is generated correctly
    matrix, fig = task_func(L=10, M=10, N=10, audio_file='/path/to/audio/file.wav')
    assert fig.shape == (10, 10)

    # Test case 4: Ensure the spectrogram is normalized correctly
    matrix, fig = task_func(L=10, M=10, N=10, audio_file='/path/to/audio/file.wav')
    assert np.allclose(np.max(matrix), np.max(fig))

    # Test case 5: Ensure the spectrogram is plotted correctly
    matrix, fig = task_func(L=10, M=10, N=10, audio_file='/path/to/audio/file.wav')
    assert plt.gcf() == fig