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
from kinow_client.models.gift import Gift


class TestGift(unittest.TestCase):
    """ Gift unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGift(self):
        """
        Test Gift
        """
        model = kinow_client.models.gift.Gift()


if __name__ == '__main__':
    unittest.main()
