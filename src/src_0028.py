import json
import base64
from datetime import datetime
def task_func(data: dict, DATE_FORMAT = "%Y-%m-%d %H:%M:%S") -> str:
    # Adding current timestamp to the dictionary
    data['timestamp'] = datetime.now().strftime(DATE_FORMAT)
    
    # Encoding the dictionary to a JSON-formatted string and then encoding it in ASCII using base64 encoding
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')
    
    return encoded_data