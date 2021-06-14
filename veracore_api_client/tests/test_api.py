""" VeraCore API Client - veracore_api_client/api.py """
import datetime
import http.client as http
import re

import unittest

import responses

from veracore_api_client.api import VeraCore
from veracore_api_client.tests.constants import \
        LOGIN_SUCCESS_RESPONSE, \
        LOGIN_FAILURE_RESPONSE, \
        GET_ORDERS_RESPONSE
from veracore_api_client.exceptions import \
        VeraCoreRequestForbidden, \
        VeraCoreRequestError, \
        VeraCoreNoSession


class TestAPI(unittest.TestCase):
    """ Test API client class functionality """

    @responses.activate
    def _test_initialization_and_authentication(
        self, json_response=LOGIN_SUCCESS_RESPONSE):
        """ test the VeraCore class initialization and login methods """
        responses.add(
            responses.POST,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/login$'),
            json=json_response,
            status=http.OK
        )
        veracore = VeraCore(
            username='UNIT TEST',
            password='UNIT TEST',
            system_id='UNIT TEST',
            domain='rhu000.veracore.com',
            session=None,
            authentication_token=None
        )
        self.assertIsInstance(veracore, VeraCore)
        return veracore

    @responses.activate
    def test_successful_authentication(self):
        """ test the failed login authentication handling """
        veracore = self._test_initialization_and_authentication()
        self.assertTrue(veracore.check_authentication_token())

    @responses.activate
    def test_failed_authentication(
        self, json_response=LOGIN_FAILURE_RESPONSE):
        """ test the failed login authentication handling """
        responses.add(
            responses.POST,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/login$'),
            json=json_response,
            status=http.FORBIDDEN
        )
        with self.assertRaises(VeraCoreRequestForbidden):
            VeraCore(
                username='UNIT TEST',
                password='UNIT TEST',
                system_id='UNIT TEST',
                domain='rhu000.veracore.com',
                session=None,
                authentication_token=None
            )

    @responses.activate
    def test_failed_login_request(
        self, json_response={'error': 'server error'}):
        """ test failed login request handling """
        responses.add(
            responses.POST,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/login$'),
            json=json_response,
            status=http.SERVICE_UNAVAILABLE
        )
        with self.assertRaises(VeraCoreRequestError):
            VeraCore(
                username='UNIT TEST',
                password='UNIT TEST',
                system_id='UNIT TEST',
                domain='rhu000.veracore.com',
                session=None,
                authentication_token=None
            )

    @responses.activate
    def test_retrieving_orders(
        self, json_response=GET_ORDERS_RESPONSE):
        """ test retrieving orders """
        veracore = self._test_initialization_and_authentication()

        responses.add(
            responses.GET,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/orders.*$'),
            json=json_response,
            status=http.OK
        )
        orders = veracore.get_orders(
            order_status='Unprocessed',
            shipping_label_status='Exists',
            single_piece=True,
            carrier_code='FEDEX',
            stream='HI / AK - Air Shipping-5#Ice - M-Tu',
            stream_start=datetime.datetime.strptime(
                '2021-06-01T00:00:00', '%Y-%m-%dT%H:%M:%S'
            ),
            stream_end=datetime.datetime.strptime(
                '2021-07-01T00:00:00', '%Y-%m-%dT%H:%M:%S'
            )
        )
        self.assertIsInstance(orders, list)
        self.assertEqual(len(orders), 1)
        self.assertEqual(
            orders[0].get('CurrentOrderStatus', None), 'Unprocessed')

    @responses.activate
    def test_failed_authentication_when_getting_orders(
        self, json_response={'error': 'not authenticated'}):
        """ test the failed login authentication handling """
        veracore = self._test_initialization_and_authentication()
        responses.add(
            responses.GET,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/orders.*$'),
            json=json_response,
            status=http.FORBIDDEN
        )
        with self.assertRaises(VeraCoreRequestForbidden):
            veracore.get_orders(order_status='Unprocessed')

    @responses.activate
    def test_failed_request_when_getting_orders(
        self, json_response={'error': 'server error'}):
        """ test failed login request handling """
        veracore = self._test_initialization_and_authentication()
        responses.add(
            responses.GET,
            # pylint: disable=line-too-long
            re.compile(r'^https://rhu000.veracore.com/VeraCore/Public.Api/api/orders.*$'),
            json=json_response,
            status=http.SERVICE_UNAVAILABLE
        )
        with self.assertRaises(VeraCoreRequestError):
            veracore.get_orders(order_status='Unprocessed')

    @responses.activate
    def test_stale_session_when_getting_orders(self):
        """ test failed login request handling """
        veracore = self._test_initialization_and_authentication()
        veracore.authentication_token_expiration = \
            datetime.datetime.now() - datetime.timedelta(days=1)
        with self.assertRaises(VeraCoreNoSession):
            veracore.get_orders(order_status='Unprocessed')
