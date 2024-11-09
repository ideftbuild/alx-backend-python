#!/usr/bin/env python3
"""Module: test_utils"""
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """Test access_nested_map"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}},  ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected results
        for multiple nested maps
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises a KeyError when an
        invalid path is provided."""
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Test get_json"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected payload from a given URL."""
        mock_response = Mock()  # response object of requests.get()
        # return value of json()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
