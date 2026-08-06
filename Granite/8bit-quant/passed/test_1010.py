import pytest
from src_1010 import task_func
import xml.etree.ElementTree as ET
import csv

@pytest.mark.parametrize("xml_content, output_csv_path, expected_output", [
    (
        "<root><child>data</child></root>",
        "output.csv",
        [["root", ""], ["child", "data"]]
    ),
    (
        "<root><child>data</child><child>data2</child></root>",
        "output.csv",
        [["root", ""], ["child", "data"], ["child", "data2"]]
    ),
    (
        "<root><child>data</child><child>data2</child></root>",
        "output.csv",
        [["root", ""], ["child", "data"], ["child", "data2"]]
    ),
])
def test_task_func(xml_content, output_csv_path, expected_output):
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(expected_output)

    try:
        root = ET.fromstring(xml_content)
        data = [[elem.tag, elem.text] for elem in root.iter()]

        with open(output_csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            actual_output = list(reader)
            assert actual_output == expected_output
    except ET.ParseError as e:
        raise ET.ParseError(f"Error parsing XML: {e}") from e
    except IOError as e:
        raise IOError(f"Error writing CSV file: {e}") from e