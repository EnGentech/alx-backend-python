#!/usr/bin/env python3
"""
test cases
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()
