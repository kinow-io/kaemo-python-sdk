# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.74
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.genders_api import GendersApi


class TestGendersApi(unittest.TestCase):
    """ GendersApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.genders_api.GendersApi()

    def tearDown(self):
        pass

    def test_get_genders(self):
        """
        Test case for get_genders

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
