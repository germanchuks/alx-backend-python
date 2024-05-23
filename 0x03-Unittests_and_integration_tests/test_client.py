#!/usr/bin/env python3
"""Module for Unittests and Integration Tests"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unittests for client.GithubOrgClient."""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """
        Test TestGithubOrgClient.org to ensure it returns the correct value.
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
        Test TestGithubOrgClient.public_repos_url to ensure it returns the
        correct value based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
