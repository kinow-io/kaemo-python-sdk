# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.35
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_create_request import CustomerCreateRequest


class TestCustomerCreateRequest(unittest.TestCase):
    """ CustomerCreateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerCreateRequest(self):
        """
        Test CustomerCreateRequest
        """
        model = kinow_client.models.customer_create_request.CustomerCreateRequest()


if __name__ == '__main__':
    unittest.main()
