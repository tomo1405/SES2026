python
import inspect
import pandas as pd
import pytest

def task_func(f_list, file_path):
    
    if not all(callable(f) for f in f_list):
        raise ValueError("All elements in f_list must be callable functions.")
    if not f_list:
        raise ValueError("f_list should not be empty.")
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")


    func_info = []
    for f in f_list:
        spec = inspect.getfullargspec(f)
        is_lambda = lambda x: x.__name__ == (lambda: None).__name__
        func_info.append([
            f.__name__, 
            len(spec.args), 
            spec.defaults, 
            spec.annotations, 
            is_lambda(f)
        ])

    df = pd.DataFrame(func_info, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")

def test_task_func():
    f_list = [lambda x: x+1, lambda x: x*2]
    file_path = 'test.csv'
    task_func(f_list, file_path)
    assert os.path.exists(file_path)
    os.remove(file_path)

    f_list = [lambda x: x+1, lambda x: x*2, lambda x: x**3]
    file_path = 'test.csv'
    with pytest.raises(ValueError):
        task_func(f_list, file_path)
    assert not os.path.exists(file_path)

    f_list = []
    file_path = 'test.csv'
    with pytest.raises(ValueError):
        task_func(f_list, file_path)
    assert not os.path.exists(file_path)

    f_list = [lambda x: x+1, lambda x: x*2]
    file_path = 123
    with pytest.raises(ValueError):
        task_func(f_list, file_path)
    assert not os.path.exists(file_path)