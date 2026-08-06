import pandas as pd
from itertools import cycle
from random import randint, seed
from pytest import raises

def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):

    if len(students) == 0:
        raise ValueError("The students list should contain at least one student.")

    seed(rng_seed)

    student_cycle = cycle(students)
    grade_data = []

    for _ in range(n_grades):
        student = next(student_cycle)
        grade = randint(min(grade_range), max(grade_range))
        grade_data.append([student, grade])

    grade_df = pd.DataFrame(grade_data, columns=['Student', 'Grade'])

    return grade_df

def test_task_func():
    # Test case 1: Test with no students
    with raises(ValueError):
        task_func(n_grades=5, students=[])

    # Test case 2: Test with valid input
    grade_df = task_func(n_grades=5, students=['Alice', 'Bob'], grade_range=range(1, 6), rng_seed=42)
    assert grade_df.shape == (5, 2)
    assert grade_df['Student'].unique().size == 2
    assert grade_df['Grade'].min() >= 1
    assert grade_df['Grade'].max() <= 5

    # Test case 3: Test with different number of grades
    grade_df = task_func(n_grades=10, students=['Alice', 'Bob'], grade_range=range(1, 6), rng_seed=42)
    assert grade_df.shape == (10, 2)