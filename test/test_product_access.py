# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.3.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_access import ProductAccess


class TestProductAccess(unittest.TestCase):
    """ ProductAccess unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAccess(self):
        """
        Test ProductAccess
        """
        model = kinow_client.models.product_access.ProductAccess()


if __name__ == '__main__':
    unittest.main()
