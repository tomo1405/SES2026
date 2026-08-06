python
import random
import string
import hashlib
import time

def task_func(data_dict: dict, seed=0) -> dict:
    random.seed(seed)
    # Constants
    SALT_LENGTH = 5
    
    # Add the key 'a' with value 1
    data_dict.update(dict(a=1))

    # Generate a random salt
    salt = ''.join(random.choice(string.ascii_lowercase) for _ in range(SALT_LENGTH))

    # Concatenate the salt with the values and hash the concatenated string
    for key in data_dict.keys():
        data_dict[key] = hashlib.sha256((str(data_dict[key]) + salt).encode()).hexdigest()

    # Timestamp the process
    data_dict['timestamp'] = time.time()

    return data_dict

def test_task_func():
    # Test case 1
    data_dict = {'name': 'John', 'age': 30}
    result = task_func(data_dict)
    assert result['name'] == hashlib.sha256(('John' + 'abcde').encode()).hexdigest()
    assert result['age'] == hashlib.sha256(('30' + 'abcde').encode()).hexdigest()
    assert result['a'] == 1
    assert isinstance(result['timestamp'], float)

    # Test case 2
    data_dict = {'name': 'Jane', 'age': 25}
    result = task_func(data_dict, seed=1)
    assert result['name'] == hashlib.sha256(('Jane' + 'fghij').encode()).hexdigest()
    assert result['age'] == hashlib.sha256(('25' + 'fghij').encode()).hexdigest()
    assert result['a'] == 1
    assert isinstance(result['timestamp'], float)

    # Test case 3
    data_dict = {'name': 'Bob', 'age': 40}
    result = task_func(data_dict, seed=2)
    assert result['name'] == hashlib.sha256(('Bob' + 'klmno').encode()).hexdigest()
    assert result['age'] == hashlib.sha256(('40' + 'klmno').encode()).hexdigest()
    assert result['a'] == 1
    assert isinstance(result['timestamp'], float)