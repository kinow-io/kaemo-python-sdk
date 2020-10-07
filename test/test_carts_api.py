# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.carts_api import CartsApi


class TestCartsApi(unittest.TestCase):
    """ CartsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.carts_api.CartsApi()

    def tearDown(self):
        pass

    def test_add_product_to_cart(self):
        """
        Test case for add_product_to_cart

        
        """
        pass

    def test_attach_cart_rule_to_cart(self):
        """
        Test case for attach_cart_rule_to_cart

        
        """
        pass

    def test_attach_cart_to_customer(self):
        """
        Test case for attach_cart_to_customer

        
        """
        pass

    def test_create_cart(self):
        """
        Test case for create_cart

        
        """
        pass

    def test_delete_cart(self):
        """
        Test case for delete_cart

        
        """
        pass

    def test_delete_product_from_cart(self):
        """
        Test case for delete_product_from_cart

        
        """
        pass

    def test_detach_cart_rule_from_cart(self):
        """
        Test case for detach_cart_rule_from_cart

        
        """
        pass

    def test_empty_cart(self):
        """
        Test case for empty_cart

        
        """
        pass

    def test_get_cart(self):
        """
        Test case for get_cart

        
        """
        pass

    def test_get_carts(self):
        """
        Test case for get_carts

        
        """
        pass

    def test_get_customer_carts(self):
        """
        Test case for get_customer_carts

        
        """
        pass

    def test_get_last_cart(self):
        """
        Test case for get_last_cart

        
        """
        pass

    def test_get_losts_carts(self):
        """
        Test case for get_losts_carts

        
        """
        pass

    def test_get_payment_url(self):
        """
        Test case for get_payment_url

        
        """
        pass

    def test_get_price(self):
        """
        Test case for get_price

        
        """
        pass

    def test_prepare_payment(self):
        """
        Test case for prepare_payment

        
        """
        pass

    def test_update_cart(self):
        """
        Test case for update_cart

        
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
