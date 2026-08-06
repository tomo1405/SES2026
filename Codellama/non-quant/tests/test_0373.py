import glob
import re


def test_task_func():
    directory_path = 'path/to/directory'
    docx_files = glob.glob(directory_path + '/*.docx')
    processed_files = 0

    for docx_file in docx_files:
        document = Document(docx_file)

        for paragraph in document.paragraphs:
            paragraph.text = re.sub(r'(?<!\\)"', r'\"', paragraph.text)

        document.save(docx_file)
        processed_files += 1

    assert processed_files == 1