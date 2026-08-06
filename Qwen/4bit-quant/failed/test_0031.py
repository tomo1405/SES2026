import pytest
from src_0031 import task_func

def test_task_func_valid_json():
    # Arrange
    file_path = 'test_data/valid.json'
    attribute = 'name'
    
    # Act & Assert
    assert task_func(file_path, attribute) == 'John Doe'

def test_task_func_missing_file():
    # Arrange
    file_path = 'non_existent_file.json'
    attribute = 'name'
    
    # Act & Assert
    with pytest.raises(ValueError, match=f'{file_path} does not exist.'):
        task_func(file_path, attribute)

def test_task_func_missing_required_field():
    # Arrange
    file_path = 'test_data/missing_name.json'
    attribute = 'name'
    
    # Act & Assert
    with pytest.raises(ValueError, match='name is missing from the JSON object.'):
        task_func(file_path, attribute)

def test_task_func_invalid_type():
    # Arrange
    file_path = 'test_data/invalid_age_type.json'
    attribute = 'age'
    
    # Act & Assert
    with pytest.raises(ValueError, match='age is not of type <class \'int\'>.'):
        task_func(file_path, attribute)

def test_task_func_invalid_email():
    # Arrange
    file_path = 'test_data/invalid_email.json'
    attribute = 'email'
    
    # Act & Assert
    with pytest.raises(ValueError, match='Email is not valid.'):
        task_func(file_path, attribute)

def test_task_func_valid_email():
    # Arrange
    file_path = 'test_data/valid_email.json'
    attribute = 'email'
    
    # Act & Assert
    assert task_func(file_path, attribute) == 'john.doe@example.com'