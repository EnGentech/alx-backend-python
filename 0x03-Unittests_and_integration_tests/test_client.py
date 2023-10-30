#!/usr/bin/env python3
"""
test cases
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('abc', ),
        ('google', )
    ])
    @patch('client.get_json')
    def test_org(self, passed, mock_org):
        """test org case"""
        test_class = GithubOrgClient(passed)
        ps = f'https://api.github.com/orgs/{passed}'
        test_class.org()
        mock_org.assert_called_once_with(ps)


    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
