python
import pandas as pd
from datetime import datetime
import pytest

def task_func(data, date_format, country, country_codes=None):
    default_country_codes = {
        'Russia': 'ru_RU',
        'Germany': 'de_DE',
        'France': 'fr_FR',
        'Spain': 'es_ES',
        'Italy': 'it_IT'
    }

    if country_codes is None:
        country_codes = default_country_codes

    if not isinstance(data, pd.DataFrame) or not isinstance(date_format, str) or not isinstance(country_codes, dict):
        raise ValueError("Invalid input types.")
    if country not in country_codes:
        raise ValueError(f"Country '{country}' not found in country codes.")

    try:
        data['parsed_dates'] = data['dates'].apply(lambda x: datetime.strptime(x, date_format).date())
    except ValueError:
        raise ValueError("Date format mismatch.")

    ax = data['parsed_dates'].hist()
    ax.set(title='Date Distribution', ylabel='Frequency')
    return ax

def test_task_func():
    # Test case 1: Valid input types and country code
    data = pd.DataFrame({'dates': ['2021-01-01', '2021-01-02', '2021-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Germany'
    country_codes = {'Germany': 'de_DE', 'Spain': 'es_ES'}
    ax = task_func(data, date_format, country, country_codes)
    assert ax.get_title() == 'Date Distribution'
    assert ax.get_ylabel() == 'Frequency'

    # Test case 2: Invalid input types
    data = 'not a dataframe'
    date_format = '%Y-%m-%d'
    country = 'Germany'
    country_codes = {'Germany': 'de_DE', 'Spain': 'es_ES'}
    with pytest.raises(ValueError) as e:
        task_func(data, date_format, country, country_codes)
    assert str(e.value) == 'Invalid input types.'

    # Test case 3: Invalid country code
    data = pd.DataFrame({'dates': ['2021-01-01', '2021-01-02', '2021-01-03']})
    date_format = '%Y-%m-%d'
    country = 'USA'
    country_codes = {'Germany': 'de_DE', 'Spain': 'es_ES'}
    with pytest.raises(ValueError) as e:
        task_func(data, date_format, country, country_codes)
    assert str(e.value) == "Country 'USA' not found in country codes."

    # Test case 4: Invalid date format
    data = pd.DataFrame({'dates': ['2021-01-01', '2021-01-02', '2021-01-03']})
    date_format = '%Y/%m/%d'
    country = 'Germany'
    country_codes = {'Germany': 'de_DE', 'Spain': 'es_ES'}
    with pytest.raises(ValueError) as e:
        task_func(data, date_format, country, country_codes)
    assert str(e.value) == "Date format mismatch."