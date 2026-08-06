import pytest
from src_0950 import task_func

def test_task_func():
    rows = 5
    columns = 3
    seed = 123
    expected_output = pd.DataFrame([[0.5488135, 0.71518934, 0.60276335],
                                  [0.4236548, 0.64589411, 0.83205029],
                                  [0.89171435, 0.96366788, 0.28737651],
                                  [0.69198646, 0.43935068, 0.5673442 ],
                                  [0.92667104, 0.57804177, 0.77815127]])
    np.random.seed(seed)
    output = task_func(rows, columns, seed)
    assert np.allclose(output, expected_output)