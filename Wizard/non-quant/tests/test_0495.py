python
import pytest
from src_0495 import task_func
from faker import Faker
from datetime import datetime
import pytz
import re

def test_task_func():
    epoch_milliseconds = 1631414400000
    seed = 0
    timezones = ["UTC"]

    Faker.seed(seed)

    faker_instance = Faker()

    event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    event_name = faker_instance.unique.first_name()

    validated_timezones = []
    utc_offset_regex = r"^UTC([+-])(0[0-9]|1[0-4]):([0-5][0-9])$"
    for tz in timezones:
        if (
            (tz == "UTC")
            or (re.match(utc_offset_regex, tz))
            or (tz in pytz.all_timezones)
        ):
            validated_timezones.append(tz)
    if not validated_timezones:
        validated_timezones = ["UTC"]

    timezone = faker_instance.random_element(elements=(validated_timezones))

    event_schedule = {
        event_name: [
            {
                "date": event_datetime.date(),
                "time": event_datetime.time(),
                "timezone": timezone,
            }
        ]
    }

    assert task_func(epoch_milliseconds, seed, timezones) == event_schedule