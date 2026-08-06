import pytest
from src_1010 import task_func
import xml.etree.ElementTree as ET
import csv
import io

def test_task_func_valid_xml():
    xml_content = """<root><elem1>text1</elem1><elem2>text2</elem2></root>"""
    output_csv_path = "test_output.csv"
    task_func(xml_content=xml_content, output_csv_path=output_csv_path)
    
    with open(output_csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        assert data == [['elem1', 'text1'], ['elem2', 'text2']]

def test_task_func_invalid_xml():
    xml_content = "<invalid_xml>"
    output_csv_path = "test_output.csv"
    with pytest.raises(ET.ParseError):
        task_func(xml_content=xml_content, output_csv_path=output_csv_path)

def test_task_func_io_error():
    xml_content = "<root><elem1>text1</elem1><elem2>text2</elem2></root>"
    output_csv_path = "/invalid_path/test_output.csv"
    with pytest.raises(IOError):
        task_func(xml_content=xml_content, output_csv_path=output_csv_path)