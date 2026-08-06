import pytest
from src_0118 import task_func

def test_task_func():
    # Test 1: num_of_students is positive
    num_of_students = 10
    df = task_func(num_of_students)
    assert len(df) == num_of_students

    # Test 2: num_of_students is negative
    num_of_students = -10
    with pytest.raises(ValueError):
        task_func(num_of_students)

    # Test 3: name_list is not None
    name_list = ['Alice', 'Bob', 'Charlie']
    df = task_func(num_of_students, name_list=name_list)
    assert len(df) == num_of_students
    assert all(df['Name'].isin(name_list))

    # Test 4: gender_list is not None
    gender_list = ['Male', 'Female']
    df = task_func(num_of_students, gender_list=gender_list)
    assert len(df) == num_of_students
    assert all(df['Gender'].isin(gender_list))

    # Test 5: age_range is not None
    age_range = (10, 20)
    df = task_func(num_of_students, age_range=age_range)
    assert len(df) == num_of_students
    assert all(df['Age'].between(age_range[0], age_range[1]))

    # Test 6: score_range is not None
    score_range = (50, 100)
    df = task_func(num_of_students, score_range=score_range)
    assert len(df) == num_of_students
    assert all(df['Score'].between(score_range[0], score_range[1]))

    # Test 7: seed is not None
    seed = 42
    df = task_func(num_of_students, seed=seed)
    assert len(df) == num_of_students
    assert all(df['Name'].isin(name_list))
    assert all(df['Gender'].isin(gender_list))
    assert all(df['Age'].between(age_range[0], age_range[1]))
    assert all(df['Score'].between(score_range[0], score_range[1]))