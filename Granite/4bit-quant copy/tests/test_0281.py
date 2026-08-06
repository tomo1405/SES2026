import pytest
from src_0281 import task_func

@pytest.mark.parametrize("signal, precision, seed, expected_output", [
    (
        [1, 2, 3, 4, 5],  # signal
        2,  # precision
        777,  # seed
        ([-3.54, -1.54, 0.46, 2.46, 4.46], None)  # expected output
    ),
    (
        [5, 4, 3, 2, 1],  # signal
        1,  # precision
        777,  # seed
        ([4.8, 3.2, 1.6, -0.0, -1.6], None)  # expected output
    ),
])
def test_task_func(signal, precision, seed, expected_output):
    np.random.seed(seed)
    output = task_func(signal, precision, seed)
    assert output == expected_output