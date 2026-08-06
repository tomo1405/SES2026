import pytest
from src_0997 import task_func

def test_task_func():
    url = "https://www.example.com"
    file_name = "Output.txt"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else None
    data = {"title": title}
    json_data = json.dumps(data)
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(json_data + "\n")
    assert task_func(url, file_name) == file_name
    with open(file_name, "r", encoding="utf-8") as f:
        assert json.loads(f.readline()) == data