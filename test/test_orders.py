# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.orders import Orders


class TestOrders(unittest.TestCase):
    """ Orders unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrders(self):
        """
        Test Orders
        """
        model = kaemo_client.models.orders.Orders()


if __name__ == '__main__':
    unittest.main()
