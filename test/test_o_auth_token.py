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
from kinow_client.models.o_auth_token import OAuthToken


class TestOAuthToken(unittest.TestCase):
    """ OAuthToken unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOAuthToken(self):
        """
        Test OAuthToken
        """
        model = kinow_client.models.o_auth_token.OAuthToken()


if __name__ == '__main__':
    unittest.main()
