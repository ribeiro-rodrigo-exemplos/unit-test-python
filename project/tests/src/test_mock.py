import unittest
from unittest.mock import Mock


class MockTestCase(unittest.TestCase):

    def test_mock_json(self):
        json = Mock()
        json.loads('{"key":"value"}')

        json.loads.assert_called()
        json.loads.assert_called_once()
        json.loads.assert_called_with('{"key":"value"}')
        json.loads.assert_called_once_with('{"key":"value"}')

        print(json.loads.call_count)
        print(json.loads.call_args)
        print(json.loads.call_args_list)
        print(json.method_call)

