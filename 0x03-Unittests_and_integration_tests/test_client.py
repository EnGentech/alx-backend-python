#!/usr/bin/env python3
"""
test cases
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from clients import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('abc', ),
        ('google', )
    ])
    @patch('clients.get_json')
    def test_org(self, passed, mock_org):
        """Test org case"""
        test_class = GithubOrgClient(passed)
        test_class.org()
        mock_org.assert_called_once_with(f'https://api.github.com/orgs/{passed}')
