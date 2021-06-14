""" VeraCore API Client - veracore_api_client/exceptions.py """
import unittest

from veracore_api_client.exceptions import \
        VeraCoreException, \
        VeraCoreRequestForbidden, \
        VeraCoreRequestError, \
        VeraCoreNoSession


class TestExceptions(unittest.TestCase):
    """Tests for exception class errors"""

    def test_exception_base_class(self):
        """tests the base class"""
        url = 'https://test'
        content = 'test-exception'
        error = VeraCoreException(
            url=url, status='500',
            resource_name='Unit Test',
            content=content
        )
        self.assertEqual(
            error.__str__(),
            'Unknown error occurred for %s. Response content: %s' % (
                url, content
            )
        )

    def test_forbidden_exception(self):
        """tests the request forbidden exception class"""
        url = 'https://test'
        content = 'test-exception'
        error = VeraCoreRequestForbidden(
            url=url, status='403',
            resource_name='Unit Test',
            content=content
        )
        self.assertEqual(
            error.__str__(),
            'Request refused for %s. Response content: %s' % (
                url, content
            )
        )

    def test_request_error_exception(self):
        """tests the request error exception class"""
        url = 'https://test'
        status = '500'
        content = 'test-exception'
        error = VeraCoreRequestError(
            url=url, status=status,
            resource_name='Unit Test',
            content=content
        )
        self.assertEqual(
            error.__str__(),
            'Request to %s has failed with status %s. %s' % (
                url, status, content
            )
        )

    def test_no_session_exception(self):
        """tests the missing session exception class"""
        url = 'https://test'
        status = None
        content = 'test-exception'
        error = VeraCoreNoSession(
            url=url, status=status,
            resource_name='Unit Test',
            content=content
        )
        self.assertEqual(
            error.__str__(),
            # pylint: disable=line-too-long
            'No valid authentication token exists when attempting to call %s. %s' % (
                url, content
            )
        )
