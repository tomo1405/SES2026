import pytest
from src_0403 import task_func

def test_task_func():
    pattern = r'[a-zA-Z]+'
    response = requests.get(API_URL)
    data = json.loads(response.text)
    matched_data = [re.findall(pattern, str(item)) for item in data['data']]
    with open('matched_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(matched_data)
    assert os.path.abspath('matched_data.csv') == 'matched_data.csv'