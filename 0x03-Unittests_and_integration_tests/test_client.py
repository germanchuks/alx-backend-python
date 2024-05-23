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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "Hello World!!"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [i["name"] for i in payloads]
            self.assertEqual(result, expected)

            mock_json.called_with_once()
            mock_public.called_with_once()
