""" VeraCore API Client - veracore_api_client/__version__.py """
import unittest

from veracore_api_client.__version__ import \
        __title__, \
        __description__, \
        __url__, \
        __version__, \
        __author__, \
        __author_email__, \
        __license__, \
        __maintainer__, \
        __maintainer_email__, \
        __keywords__, \
        get_version_information


class TestVersionData(unittest.TestCase):
    """Tests for required version information"""

    def test_version_variables(self):
        """Ensure that all variables exist with values"""
        self.assertIsNotNone(__title__)
        self.assertIsNotNone(__description__)
        self.assertIsNotNone(__url__)
        self.assertIsNotNone(__version__)
        self.assertIsNotNone(__author__)
        self.assertIsNotNone(__author_email__)
        self.assertIsNotNone(__license__)
        self.assertIsNotNone(__maintainer__)
        self.assertIsNotNone(__maintainer_email__)
        self.assertIsNotNone(__keywords__)

    def test_version_output(self):
        """Verify version information"""
        self.assertEqual(
            get_version_information(display=False),
            # pylint: disable=line-too-long
            'VeraCore API Python Client: Version {version}. Released under a {license} license. Author: {author}.'.format(
                version=__version__, license=__license__, author=__author__
            )
        )
        self.assertEqual(
            get_version_information(display=True, debug=True),
            # pylint: disable=line-too-long
            'VeraCore API Python Client: Version {version}. Released under a {license} license. Author: {author}.'.format(
                version=__version__, license=__license__, author=__author__
            )
        )
