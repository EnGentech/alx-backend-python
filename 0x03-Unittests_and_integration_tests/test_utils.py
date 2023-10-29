#!/usr/bin/env python3
"""
test cases
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """A test case for nested_keys"""
        obtained = access_nested_map(nested_map, path)
        self.assertEqual(obtained, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, map):
        """An assertRaise exception test case"""
        with self.assertRaises(KeyError) as invalid:
            obtained = access_nested_map(nested_map, map)

            self.assertEqual(obtained, str(invalid.exception))


class TestGetJson(unittest.TestCase):
    """GetJson test"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ("http://holberton.io", {'payload': False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test json() request return function"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        response = get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Test class"""
    def test_memoize(self):
        """test memoize method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        instance = TestClass()
        with patch.object(instance, "a_method") as mock_func:
            mock_func.return_value = 50

            first_call = instance.a_property
            second_call = instance.a_property

            mock_func.assert_called_once()
            self.assertEqual(first_call, 50)
            self.assertEqual(second_call, 50)


if __name__ == '__main__':
    unittest.main()
