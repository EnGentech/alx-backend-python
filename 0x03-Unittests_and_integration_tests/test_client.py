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
        """test"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock:
            json_dict = {'repos_url': 'hello world'}
            mock.return_value = json_dict
            test = GithubOrgClient('check')
            response = test._public_repos_url
            self.assertEqual(response, json_dict['repos_url'])


if __name__ == '__main__':
    unittest.main()
