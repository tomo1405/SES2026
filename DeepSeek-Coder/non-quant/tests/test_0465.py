import pytest
from src_0465 import task_func

def test_task_func():
    # Test case 1: Test with a datetime object
    from datetime import datetime
    from decimal import Decimal
    my_obj = {"date": datetime.now(), "amount": Decimal('123.45')}
    result = task_func(my_obj)
    assert 'datetime' in result
    assert 'Decimal' in result

    # Test case 2: Test with a different datetime and Decimal
    from datetime import datetime
    from decimal import Decimal
    my_obj = {"date": datetime.now(), "amount": Decimal('678.90')}
    result = task_func(my_obj)
    assert 'datetime' in result
    assert 'Decimal' in result