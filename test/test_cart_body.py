# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.80
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cart_body import CartBody


class TestCartBody(unittest.TestCase):
    """ CartBody unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartBody(self):
        """
        Test CartBody
        """
        model = kinow_client.models.cart_body.CartBody()


if __name__ == '__main__':
    unittest.main()
