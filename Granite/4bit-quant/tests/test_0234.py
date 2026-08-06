from src_0234 import task_func


def test_task_func():
    obj_list = [Object(value=i) for i in range(100)]
    ax = task_func(obj_list, 'value')
    assert ax is not None
    assert ax.get_title() == 'Histogram of attribute values'
    assert ax.get_xlabel() == 'Attribute Value'
    assert ax.get_ylabel() == 'Count'