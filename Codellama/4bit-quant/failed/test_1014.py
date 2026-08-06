import pytest
from src_1014 import task_func

def test_task_func():
    # Test that the function returns the correct number of links
    url = "https://www.example.com/page1"
    base_url = "https://www.example.com"
    csv_file = "scraped_data.csv"
    expected_links = 5
    actual_links = task_func(url, base_url, csv_file)
    assert actual_links == expected_links

    # Test that the function writes the correct links to the CSV file
    with open(csv_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        actual_links = [link for link in reader]
    assert actual_links == expected_links

    # Test that the function handles invalid URLs correctly
    url = "https://www.example.com/page2"
    base_url = "https://www.example.com"
    csv_file = "scraped_data.csv"
    expected_links = 0
    actual_links = task_func(url, base_url, csv_file)
    assert actual_links == expected_links

    # Test that the function handles invalid CSV file paths correctly
    url = "https://www.example.com/page3"
    base_url = "https://www.example.com"
    csv_file = "invalid_path.csv"
    expected_links = 0
    actual_links = task_func(url, base_url, csv_file)
    assert actual_links == expected_links