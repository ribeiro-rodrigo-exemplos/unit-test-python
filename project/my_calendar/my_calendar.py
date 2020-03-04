from datetime import datetime
import requests


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5