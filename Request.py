import requests
from config import (URL, API_KEY)


def get_request(params):
    response = requests.get(URL, params=params, headers=API_KEY)
    return response
