from collections import defaultdict
import re
def task_func(word: str) -> dict:
    # Sanitize the word to include only alphabetic characters
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    return occurrences