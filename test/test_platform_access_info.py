# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.53
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.platform_access_info import PlatformAccessInfo


class TestPlatformAccessInfo(unittest.TestCase):
    """ PlatformAccessInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlatformAccessInfo(self):
        """
        Test PlatformAccessInfo
        """
        model = kinow_client.models.platform_access_info.PlatformAccessInfo()


if __name__ == '__main__':
    unittest.main()
