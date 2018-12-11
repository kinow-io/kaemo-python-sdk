# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.64
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.payment_modules_api import PaymentModulesApi


class TestPaymentModulesApi(unittest.TestCase):
    """ PaymentModulesApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.payment_modules_api.PaymentModulesApi()

    def tearDown(self):
        pass

    def test_get_payment_modules(self):
        """
        Test case for get_payment_modules

        
        """
        pass

    def test_get_payment_url(self):
        """
        Test case for get_payment_url

        
        """
        pass

    def test_validate_cart(self):
        """
        Test case for validate_cart

        
        """
        pass

    def test_validate_free_order(self):
        """
        Test case for validate_free_order

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
