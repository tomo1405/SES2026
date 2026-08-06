from datetime import datetime
import pandas as pd
# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    data = []

    for time_string in time_strings:
        utc_time = datetime.strptime(time_string, TIME_FORMAT)
        converted_time = utc_time.replace(tzinfo=ZoneInfo("UTC")).astimezone(
            ZoneInfo(target_tz)
        )
        data.append([time_string, converted_time.strftime(TIME_FORMAT)])

    df = pd.DataFrame(data, columns=["Original Time", "Converted Time"])
    return df