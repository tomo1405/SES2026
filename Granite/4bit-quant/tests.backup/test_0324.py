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
    text = "Alice[tag1] Bob[tag2] Charlie"
    word_freqs, means = task_func(text, num_gaussians=2)
    assert isinstance(word_freqs, dict)
    assert isinstance(means, np.ndarray)
    assert len(means.shape) == 2
    assert word_freqs == {'Alice': 1, 'Bob': 1, 'Charlie': 1}
    assert means.shape == (2, 1)

def test_task_func_invalid_num_gaussians():
    text = "Alice[tag1] Bob[tag2] Charlie"
    with pytest.raises(ValueError):
        task_func(text, num_gaussians=0)

def test_task_func_invalid_num_gaussians_2():
    text = "Alice[tag1] Bob[tag2] Charlie"
    with pytest.raises(Exception):
        task_func(text, num_gaussians=3)