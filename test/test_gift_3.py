# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.gift_3 import Gift3


class TestGift3(unittest.TestCase):
    """ Gift3 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGift3(self):
        """
        Test Gift3
        """
        model = kinow_client.models.gift_3.Gift3()


if __name__ == '__main__':
    unittest.main()
