# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.cart_rules import CartRules


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
        model = kaemo_client.models.cart_rules.CartRules()


if __name__ == '__main__':
    unittest.main()
