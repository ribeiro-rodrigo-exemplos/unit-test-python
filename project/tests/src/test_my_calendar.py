import datetime
from requests.exceptions import Timeout
import unittest
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()
requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


class MyCalendarTestCase(unittest.TestCase):

    def test_my_calendar(self):
        datetime.datetime.today.return_value = tuesday
        self.assertTrue(is_weekday())

        datetime.datetime.today.return_value = saturday
        self.assertTrue(not is_weekday())

    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holidays_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/14': 'Independence Day',
        }

        requests.get.side_effect = [Timeout, response_mock]

        with self.assertRaises(Timeout):
            get_holidays()

        self.assertEqual(get_holidays()['12/25'], 'Christmas')
        self.assertEqual(requests.get.call_count, 2)

