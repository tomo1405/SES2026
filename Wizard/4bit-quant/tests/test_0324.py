python
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    np.random.seed(seed)
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    words = ' '.join(names).split()
    word_freqs = Counter(words)
    if num_gaussians <= 0:
        raise ValueError('Number of Gaussians must be greater than 0.')
    if len(word_freqs) < num_gaussians:
        raise Exception('Number of Gaussians must be less than or equal to the number of unique words.')

    mixture = GaussianMixture(n_components=num_gaussians)
    mixture.fit([[freq] for freq in word_freqs.values()])
    means = mixture.means_
    return dict(word_freqs), means

def test_task_func():
    # Test case 1: Valid input
    text = 'John [Smith] Doe [Jones] John [Johnson] Smith'
    num_gaussians = 2
    seed = 42
    expected_word_freqs = {'john': 3, 'doe': 1, 'jones': 1, 'johnson': 1, 'smith': 1}
    expected_means = np.array([[1.5], [1.5]])
    actual_word_freqs, actual_means = task_func(text, num_gaussians, seed)
    assert actual_word_freqs == expected_word_freqs
    assert np.array_equal(actual_means, expected_means)

    # Test case 2: Invalid input: num_gaussians <= 0
    text = 'John [Smith] Doe [Jones] John [Johnson] Smith'
    num_gaussians = 0
    seed = 42
    try:
        task_func(text, num_gaussians, seed)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert str(e) == 'Number of Gaussians must be greater than 0.'

    # Test case 3: Invalid input: len(word_freqs) < num_gaussians
    text = 'John [Smith] Doe [Jones] John [Johnson] Smith'
    num_gaussians = 4
    seed = 42
    try:
        task_func(text, num_gaussians, seed)
        assert False, 'Expected Exception'
    except Exception as e:
        assert str(e) == 'Number of Gaussians must be less than or equal to the number of unique words.'