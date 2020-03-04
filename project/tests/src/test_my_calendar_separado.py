import unittest
from my_calendar.my_calendar import get_holidays
import requests
from requests.exceptions import Timeout
from unittest.mock import patch


class MyCalendarSeparadoTestCase(unittest.TestCase):
    @patch('my_calendar.my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    def test_get_holidays_timeout_2(self):
        with patch('my_calendar.my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    @patch.object(requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout_part_object(self, mock_requests):
        with self.assertRaises(Timeout):
            get_holidays()


