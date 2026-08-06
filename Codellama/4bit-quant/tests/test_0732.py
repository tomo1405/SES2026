from src_0732 import task_func


def test_task_func():
    data, target = task_func(DATA, TARGET)
    assert data.shape == (100, 20)
    assert target.shape == (100,)
    assert np.allclose(data, loaded_data)
    assert np.allclose(target, loaded_target)