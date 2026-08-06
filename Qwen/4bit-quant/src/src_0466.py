import json
from datetime import datetime
import numpy as np
from decimal import Decimal
def task_func(my_obj):
    
    class ComplexEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, Decimal):
                return str(obj)
            return json.JSONEncoder.default(self, obj)
    return json.dumps(my_obj, cls=ComplexEncoder)