import csv
import json
import os
import re

import requests


def test_task_func():
    pattern = r'[a-zA-Z0-9]+'
    response = requests.get(API_URL)
    data = json.loads(response.text)
    matched_data = [re.findall(pattern, str(item)) for item in data['data']]
    with open('matched_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(matched_data)
    assert os.path.exists('matched_data.csv')
    assert os.path.isfile('matched_data.csv')
    assert os.path.getsize('matched_data.csv') > 0
    os.remove('matched_data.csv')