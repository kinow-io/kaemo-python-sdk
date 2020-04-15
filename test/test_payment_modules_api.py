# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.62
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.payment_modules_api import PaymentModulesApi


class TestPaymentModulesApi(unittest.TestCase):
    """ PaymentModulesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.payment_modules_api.PaymentModulesApi()

    def tearDown(self):
        pass

    def test_get_payment_methods(self):
        """
        Test case for get_payment_methods

        
        """
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

    def test_get_pending_payments(self):
        """
        Test case for get_pending_payments

        
        """
        pass

    def test_prepare_payment(self):
        """
        Test case for prepare_payment

        
        """
        pass

    def test_update_payment_method(self):
        """
        Test case for update_payment_method

        
        """
        pass

    def test_validate_free_order(self):
        """
        Test case for validate_free_order

        
        """
        pass

    def test_validate_payment(self):
        """
        Test case for validate_payment

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
