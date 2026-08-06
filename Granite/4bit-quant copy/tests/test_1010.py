import xml.etree.ElementTree as ET
import csv
import pytest

def task_func(xml_content, output_csv_path):
    try:
        root = ET.fromstring(xml_content)
        data = [[elem.tag, elem.text] for elem in root.iter()]

        with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    except ET.ParseError as e:
        raise ET.ParseError(f"Error parsing XML: {e}") from e
    except IOError as e:
        raise IOError(f"Error writing CSV file: {e}") from e

def test_task_func():
    xml_content = "<root><elem>data</elem></root>"
    output_csv_path = "output.csv"

    try:
        task_func(xml_content, output_csv_path)
        assert True  # Test passes if no exceptions are raised
    except ET.ParseError:
        assert False  # Test fails if XML parsing error is raised
    except IOError:
        assert False  # Test fails if CSV writing error is raised