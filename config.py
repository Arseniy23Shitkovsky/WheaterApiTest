from os import getenv

URL = getenv('URL', "https://api.weather.yandex.ru/v1/forecast?")
API_KEY = getenv("KEY", {'X-Yandex-API-Key': 'yourKey'})
