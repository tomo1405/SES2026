import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from src_0168 import task_func
import pytest

@pytest.mark.parametrize("num_types,integer_range,expected_labels", [
    (5, (0, 100), ['Type1', 'Type2', 'Type3', 'Type4', 'Type5']),
    (3, (10, 20), ['Type1', 'Type2', 'Type3']),
    (7, (50, 100), ['Type1', 'Type2', 'Type3', 'Type4', 'Type5', 'Type6', 'Type7']),
])
def test_task_func(num_types, integer_range, expected_labels):
    fig, ax = task_func(num_types, integer_range)
    actual_labels = [label.get_text() for label in ax.get_xticklabels()]
    assert actual_labels == expected_labels