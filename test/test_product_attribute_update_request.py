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
from kinow_client.models.product_attribute_update_request import ProductAttributeUpdateRequest


class TestProductAttributeUpdateRequest(unittest.TestCase):
    """ ProductAttributeUpdateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttributeUpdateRequest(self):
        """
        Test ProductAttributeUpdateRequest
        """
        model = kinow_client.models.product_attribute_update_request.ProductAttributeUpdateRequest()


if __name__ == '__main__':
    unittest.main()
