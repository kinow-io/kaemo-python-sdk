# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.53
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.prepayments_api import PrepaymentsApi


class TestPrepaymentsApi(unittest.TestCase):
    """ PrepaymentsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.prepayments_api.PrepaymentsApi()

    def tearDown(self):
        pass

    def test_get_customer_prepayment_balances(self):
        """
        Test case for get_customer_prepayment_balances

        
        """
        pass

    def test_get_customer_prepayment_operations(self):
        """
        Test case for get_customer_prepayment_operations

        
        """
        pass

    def test_get_prepayment_bonus(self):
        """
        Test case for get_prepayment_bonus

        
        """
        pass

    def test_get_prepayment_bonus_list(self):
        """
        Test case for get_prepayment_bonus_list

        
        """
        pass

    def test_get_prepayment_operation(self):
        """
        Test case for get_prepayment_operation

        
        """
        pass

    def test_get_prepayment_operations(self):
        """
        Test case for get_prepayment_operations

        
        """
        pass

    def test_get_prepayment_recharge(self):
        """
        Test case for get_prepayment_recharge

        
        """
        pass

    def test_get_prepayment_recharges(self):
        """
        Test case for get_prepayment_recharges

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
