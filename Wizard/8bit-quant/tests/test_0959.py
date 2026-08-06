python
import random
import re
import pytest

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)

    def scramble_word(match):
        word = match.group(0)
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + "".join(middle) + word[-1]
        else:
            return word

    pattern = r"\b\w+\b"
    scrambled_text = re.sub(pattern, scramble_word, text)

    return scrambled_text

def test_task_func():
    # Test case 1: No seed provided
    text = "The quick brown fox jumps over the lazy dog."
    expected_output = "Tq kcwh fxbjmps vz th lzy dg."
    assert task_func(text) == expected_output

    # Test case 2: Seed provided
    text = "The quick brown fox jumps over the lazy dog."
    seed = 1234
    expected_output = "Tq kcwh fxbjmps vz th lzy dg."
    assert task_func(text, seed) == expected_output

    # Test case 3: Text contains punctuation
    text = "The quick, brown fox jumps over the lazy dog!"
    expected_output = "Tq kcwh, bfxjmps vz th lzy dg!"
    assert task_func(text) == expected_output

    # Test case 4: Text contains numbers
    text = "The quick brown fox jumps over the 123 lazy dog."
    expected_output = "Tq kcwh fxbjmps vz th 123 lzy dg."
    assert task_func(text) == expected_output

    # Test case 5: Text contains special characters
    text = "The quick brown fox jumps over the lazy dog: #$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    expected_output = "Tq kcwh fxbjmps vz th lzy dg: #$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    assert task_func(text) == expected_output

    # Test case 6: Text contains words with length <= 3
    text = "The quick brown fox jumps over the lazy dog. The dog is lazy."
    expected_output = "Tq kcwh fxbjmps vz th lzy dg. Tq dg s lzy."
    assert task_func(text) == expected_output