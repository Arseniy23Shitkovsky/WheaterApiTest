from Request import get_request
from Coordinate import MSK_LAT, MSK_LON


def test_get_msk_weather():
    params = {'lat': MSK_LAT,
              'lon': MSK_LON,
              'extra': 'true',
              'hours': 'true',
              'limit': 1,
              'lang': "ru_RU",
              }
    response = get_request(params)
    data = response.json()['info']['tzinfo']
    name_timezone = data['name']
    abbr = data['abbr']
    timezone_utc = data['offset']
    assert name_timezone == 'Europe/Moscow' and abbr == 'MSK' and timezone_utc == 10800
