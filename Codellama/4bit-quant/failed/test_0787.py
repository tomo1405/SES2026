import pytest
from src_0787 import task_func

def test_task_func():
    # Test with default values
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = None
    random_seed = None
    expected_data = [
        {'Country': 'USA', 'Product': 'Product A', 'Sales': 10},
        {'Country': 'UK', 'Product': 'Product B', 'Sales': 20},
        {'Country': 'China', 'Product': 'Product C', 'Sales': 30},
        {'Country': 'India', 'Product': 'Product D', 'Sales': 40},
        {'Country': 'Germany', 'Product': 'Product E', 'Sales': 50}
    ]
    result = task_func(n, countries, products, output_path, random_seed)
    assert result.equals(expected_data)

    # Test with custom values
    n = 5
    countries = ['France', 'Spain', 'Italy', 'Greece', 'Portugal']
    products = ['Product F', 'Product G', 'Product H', 'Product I', 'Product J']
    output_path = 'test_data.csv'
    random_seed = 42
    expected_data = [
        {'Country': 'France', 'Product': 'Product F', 'Sales': 10},
        {'Country': 'Spain', 'Product': 'Product G', 'Sales': 20},
        {'Country': 'Italy', 'Product': 'Product H', 'Sales': 30},
        {'Country': 'Greece', 'Product': 'Product I', 'Sales': 40},
        {'Country': 'Portugal', 'Product': 'Product J', 'Sales': 50}
    ]
    result = task_func(n, countries, products, output_path, random_seed)
    assert result.equals(expected_data)
    assert os.path.exists(output_path)
    os.remove(output_path)

if __name__ == '__main__':
    pytest.main()