#!/usr/bin/env python3
"""Module: test_utils"""
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(TestCase):
    """Test memoize"""

    def test_memoize(self):
        """Test that memoize memoizes a method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # patch a_method and check if it is called once
        with patch.object(
                TestClass, 'a_method', return_value=42
        ) as mock_a_method:
            test_class = TestClass()
            r = test_class.a_property, test_class.a_property
            mock_a_method.assert_called_once()
