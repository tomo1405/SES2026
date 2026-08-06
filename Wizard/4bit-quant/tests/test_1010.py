python
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
    # Test case 1: Valid XML input
    xml_content = """<root>
                        <person>
                            <name>John</name>
                            <age>30</age>
                        </person>
                        <person>
                            <name>Jane</name>
                            <age>25</age>
                        </person>
                    </root>"""
    output_csv_path = "output.csv"
    task_func(xml_content, output_csv_path)
    with open(output_csv_path, "r", encoding="utf-8") as f:
        assert f.read() == "name,age\nJohn,30\nJane,25\n"

    # Test case 2: Invalid XML input
    xml_content = """<root>
                        <person>
                            <name>John</name>
                            <age>30</age>
                        </person>
                        <person>
                            <name>Jane</name>
                            <age>25</age>
                        </person>
                    </root>"""
    output_csv_path = "output.csv"
    with pytest.raises(ET.ParseError):
        task_func(xml_content, output_csv_path + "invalid")

    # Test case 3: Invalid output file path
    xml_content = """<root>
                        <person>
                            <name>John</name>
                            <age>30</age>
                        </person>
                        <person>
                            <name>Jane</name>
                            <age>25</age>
                        </person>
                    </root>"""
    output_csv_path = "output.csv"
    with pytest.raises(IOError):
        task_func(xml_content, "/invalid/path/output.csv")