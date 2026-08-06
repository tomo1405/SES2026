import pytest
from src_0070 import task_func
import random
import matplotlib.pyplot as plt

@pytest.fixture
def mock_random_int(monkeypatch):
    def mock_randint(a, b):
        return 60000  # Fixed value for testing purposes
    monkeypatch.setattr(random, 'randint', mock_randint)

def test_task_func(mock_random_int):
    input_dict = {'EMPXX001': 3, 'EMPXX002': 2, 'NOTEMPXX001': 1}
    ax = task_func(input_dict)
    
    assert len(ax.patches) == 10  # 10 bins
    assert ax.get_title() == 'Salary Distribution in EMPXX Department'
    assert ax.get_xlabel() == 'Salary'
    assert ax.get_ylabel() == 'Number of Employees'
    
    # Check that only salaries within the range are plotted
    for patch in ax.patches:
        height = patch.get_height()
        width = patch.get_width()
        x = patch.get_x()
        assert x >= SALARY_RANGE[0]
        assert x + width <= SALARY_RANGE[1]

    # Clean up plot to avoid interference with other tests
    plt.close()