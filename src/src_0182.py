from django.http import HttpResponse
from django.conf import settings
import random
import time
def task_func(data, min_delay, max_delay):

    # Generate a random delay
    delay = random.uniform(min_delay, max_delay)

    # Wait for the delay
    time.sleep(delay)

    response = HttpResponse(data, content_type='application/json')

    return response