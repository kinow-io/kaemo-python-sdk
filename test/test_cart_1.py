# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cart_1 import Cart1


class TestCart1(unittest.TestCase):
    """ Cart1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCart1(self):
        """
        Test Cart1
        """
        model = kinow_client.models.cart_1.Cart1()


if __name__ == '__main__':
    unittest.main()
