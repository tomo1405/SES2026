import pytest
from src_0466 import task_func
import json
from datetime import datetime
import numpy as np
from decimal import Decimal

def test_task_func():
    # Test with datetime
    now = datetime.now()
    result = task_func(now)
    expected = json.dumps(now, cls=ComplexEncoder)
    assert result == expected

    # Test with numpy array
    array = np.array([1, 2, 3])
    result = task_func(array)
    expected = json.dumps(array.tolist(), cls=ComplexEncoder)
    assert result == expected

    # Test with Decimal
    decimal_value = Decimal('123.45')
    result = task_func(decimal_value)
    expected = json.dumps(str(decimal_value), cls=ComplexEncoder)
    assert result == expected

    # Test with a custom object (not supported by default JSON encoder)
    with pytest.raises(TypeError):
        task_func(object())