# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.player_configuration import PlayerConfiguration


class TestPlayerConfiguration(unittest.TestCase):
    """ PlayerConfiguration unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayerConfiguration(self):
        """
        Test PlayerConfiguration
        """
        model = kaemo_client.models.player_configuration.PlayerConfiguration()


if __name__ == '__main__':
    unittest.main()
