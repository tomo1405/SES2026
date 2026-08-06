python
import pandas as pd
import numpy as np
from random import choice, seed as set_seed
import pytest

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    if num_of_students <= 0:
        raise ValueError("num_of_students must be positive.")

    set_seed(seed)
    np.random.seed(seed)

    name_list = name_list or ['John', 'Mike', 'Sara', 'Emma', 'Nick']
    gender_list = gender_list or ['Male', 'Female']

    data = []
    for _ in range(num_of_students):
        name = choice(name_list)
        age = np.random.randint(age_range[0], age_range[1] + 1)
        gender = choice(gender_list)
        score = np.random.randint(score_range[0], score_range[1] + 1)
        data.append([name, age, gender, score])

    columns = ['Name', 'Age', 'Gender', 'Score']
    df = pd.DataFrame(data, columns=columns)
    return df

def test_task_func():
    # Test case 1: num_of_students is negative
    with pytest.raises(ValueError):
        task_func(-1)

    # Test case 2: num_of_students is zero
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 3: num_of_students is positive
    df = task_func(5)
    assert df.shape == (5, 4)
    assert df['Name'].nunique() == 5
    assert df['Age'].min() >= 15
    assert df['Age'].max() <= 20
    assert df['Gender'].nunique() == 2
    assert df['Score'].min() >= 50
    assert df['Score'].max() <= 100

    # Test case 4: name_list is empty
    df = task_func(5, name_list=[])
    assert df.shape == (5, 4)
    assert df['Name'].nunique() == 5
    assert df['Age'].min() >= 15
    assert df['Age'].max() <= 20
    assert df['Gender'].nunique() == 2
    assert df['Score'].min() >= 50
    assert df['Score'].max() <= 100

    # Test case 5: gender_list is empty
    df = task_func(5, gender_list=[])
    assert df.shape == (5, 4)
    assert df['Name'].nunique() == 5
    assert df['Age'].min() >= 15
    assert df['Age'].max() <= 20
    assert df['Gender'].nunique() == 2
    assert df['Score'].min() >= 50
    assert df['Score'].max() <= 100

    # Test case 6: age_range is invalid
    with pytest.raises(ValueError):
        task_func(5, age_range=(20, 15))

    # Test case 7: score_range is invalid
    with pytest.raises(ValueError):
        task_func(5, score_range=(100, 50))

    # Test case 8: seed is not an integer
    with pytest.raises(TypeError):
        task_func(5, seed='42')