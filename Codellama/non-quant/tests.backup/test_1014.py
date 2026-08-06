import pytest
from src_1014 import task_func

def test_task_func():
    url = "https://www.example.com/page1"
    base_url = "https://www.example.com"
    csv_file = "scraped_data.csv"

    # Test that the function returns the correct number of links
    assert task_func(url, base_url, csv_file) == 5

    # Test that the function writes the correct links to the CSV file
    with open(csv_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        links = [row[0] for row in reader]
        assert links == ["https://www.example.com/page1", "https://www.example.com/page2", "https://www.example.com/page3", "https://www.example.com/page4", "https://www.example.com/page5"]