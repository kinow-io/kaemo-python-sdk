# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customers import Customers


class TestCustomers(unittest.TestCase):
    """ Customers unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomers(self):
        """
        Test Customers
        """
        model = kinow_client.models.customers.Customers()


if __name__ == '__main__':
    unittest.main()
