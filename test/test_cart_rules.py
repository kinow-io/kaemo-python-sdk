# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.60
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cart_rules import CartRules


class TestCartRules(unittest.TestCase):
    """ CartRules unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartRules(self):
        """
        Test CartRules
        """
        model = kinow_client.models.cart_rules.CartRules()


if __name__ == '__main__':
    unittest.main()
