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
        task_func(n_grades=10, students=[])

    # Test case 2: Test with one student
    grade_df = task_func(n_grades=10, students=['Alice'])
    assert grade_df['Student'].nunique() == 1

    # Test case 3: Test with multiple students
    grade_df = task_func(n_grades=10, students=['Alice', 'Bob', 'Charlie'])
    assert grade_df['Student'].nunique() == 3

    # Test case 4: Test with different number of grades
    grade_df_1 = task_func(n_grades=10)
    grade_df_2 = task_func(n_grades=20)
    assert len(grade_df_1) < len(grade_df_2)

    # Test case 5: Test with different grade range
    grade_df_1 = task_func(n_grades=10, grade_range=range(1, 11))
    grade_df_2 = task_func(n_grades=10, grade_range=range(1, 21))
    assert grade_df_1['Grade'].max() < grade_df_2['Grade'].max()

    # Test case 6: Test with different random seed
    grade_df_1 = task_func(n_grades=10, rng_seed=123)
    grade_df_2 = task_func(n_grades=10, rng_seed=123)
    assert grade_df_1.equals(grade_df_2)

    grade_df_1 = task_func(n_grades=10, rng_seed=456)
    grade_df_2 = task_func(n_grades=10, rng_seed=456)
    assert not grade_df_1.equals(grade_df_2)