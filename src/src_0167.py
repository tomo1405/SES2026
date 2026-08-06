import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")

    country_holidays = holidays.CountryHoliday(country)
    dates = pd.date_range(start_date, end_date)
    business_days = [date for date in dates if date.weekday() < 5 and date not in country_holidays]

    return business_days