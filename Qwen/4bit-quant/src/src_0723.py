import urllib.request
import os
import re
# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'
def task_func(url):
    TARGET_FILE = 'downloaded_file.txt'
    SEARCH_PATTERN = r'\bERROR\b'

    urllib.request.urlretrieve(url, TARGET_FILE)

    with open(TARGET_FILE, 'r') as f:
        data = f.read()
    occurrences = len(re.findall(SEARCH_PATTERN, data))

    os.remove(TARGET_FILE)

    return occurrences