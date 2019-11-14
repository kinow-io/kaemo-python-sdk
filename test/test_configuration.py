# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.31
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    """ Configuration unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfiguration(self):
        """
        Test Configuration
        """
        model = kinow_client.models.configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
