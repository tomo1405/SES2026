import pytest
from src_0759 import task_func

def test_task_func_num_samples_type():
    with pytest.raises(ValueError):
        task_func(num_samples='hello')

def test_task_func_num_samples_value():
    with pytest.raises(ValueError):
        task_func(num_samples=-1)

def test_task_func_countries_type():
    with pytest.raises(ValueError):
        task_func(num_samples=10, countries=123)

def test_task_func_ages_type():
    with pytest.raises(ValueError):
        task_func(num_samples=10, ages='hello')

def test_task_func_genders_type():
    with pytest.raises(ValueError):
        task_func(num_samples=10, genders=123)

def test_task_func_rng_seed_type():
    with pytest.raises(ValueError):
        task_func(num_samples=10, rng_seed='hello')

def test_task_func_output_type():
    output = task_func(num_samples=10)
    assert isinstance(output, pd.DataFrame)

def test_task_func_output_shape():
    output = task_func(num_samples=10)
    assert output.shape == (10, 3)

def test_task_func_output_columns():
    output = task_func(num_samples=10)
    assert set(output.columns) == {'Country', 'Age', 'Gender'}

def test_task_func_output_values():
    output = task_func(num_samples=10)
    assert set(output['Country'].unique()) == {'Russia', 'China', 'USA', 'India', 'Brazil'}
    assert set(output['Age'].unique()) == set(np.arange(18, 60))
    assert set(output['Gender'].unique()) == {'Male', 'Female'}