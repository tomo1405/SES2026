import pytest
from src_0998 import task_func
import os
import zipfile
import tempfile

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    if os.path.exists(TARGET_DIR):
        for filename in os.listdir(TARGET_DIR):
            file_path = os.path.join(TARGET_DIR, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        os.rmdir(TARGET_DIR)
    if os.path.exists(TARGET_ZIP_FILE):
        os.remove(TARGET_ZIP_FILE)

def test_task_func_with_valid_zip_url():
    # Create a temporary zip file for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_zip_path = os.path.join(temp_dir, "test.zip")
        with zipfile.ZipFile(test_zip_path, 'w') as test_zip:
            test_zip.writestr("test_file.txt", "This is a test file.")
        
        # Use a local server to serve the zip file
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        import threading
        import socket
        
        class RequestHandler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=temp_dir, **kwargs)
        
        server_address = ('', 0)  # let the OS pick a free port
        httpd = HTTPServer(server_address, RequestHandler)
        server_port = httpd.server_address[1]
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()
        
        try:
            url = f"http://localhost:{server_port}/test.zip"
            result = task_func(url)
            assert result == TARGET_DIR
            assert os.path.exists(os.path.join(TARGET_DIR, "test_file.txt"))
        finally:
            httpd.shutdown()
            server_thread.join()

def test_task_func_with_invalid_url():
    invalid_url = "http://nonexistenturl.com/nonexistentfile.zip"
    with pytest.raises(urllib.error.URLError):
        task_func(invalid_url)

def test_task_func_with_non_zip_file():
    # Create a temporary text file for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a text file.")
    
    # Use a local server to serve the text file
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    import threading
    import socket
    
    class RequestHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=os.path.dirname(temp_file.name), **kwargs)
    
    server_address = ('', 0)  # let the OS pick a free port
    httpd = HTTPServer(server_address, RequestHandler)
    server_port = httpd.server_address[1]
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.start()
    
    try:
        url = f"http://localhost:{server_port}/{os.path.basename(temp_file.name)}"
        with pytest.raises(zipfile.BadZipFile):
            task_func(url)
    finally:
        httpd.shutdown()
        server_thread.join()
        os.remove(temp_file.name)