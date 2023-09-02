#!/usr/bin/env python3
""" Parameterize a unit test """
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map
import unittest
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map method from utils module
    """
    @parameterized.expand([
        nested_map = {"a": 1}, path = ("a",)
        nested_map = {"a": {"b": 2}}, path = ("a",)
        nested_map = {"a": {"b": 2}}, path = ("a", "b")
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """Tests `access_nested_map`'s output."""
        self.asertEqual(access_nested_map(nested_map), expected)

    @parameterized.expand([
        nested_map = {}, path = ("a",)
        nested_map = {"a": 1}, path = ("a", "b")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ) -> None:
        """Test access_nested_map exception """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get_json method from utils module """
    @parameterized.expamd([
        test_url = "http://example.com", test_payload = {"payload": True}
        test_url = "http://holberton.io", test_payload = {"payload": False}
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
    ) -> None:
        """ Test get_json output """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` method from utils module."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()