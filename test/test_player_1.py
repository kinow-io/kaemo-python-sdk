# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.81
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.player_1 import Player1


class TestPlayer1(unittest.TestCase):
    """ Player1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayer1(self):
        """
        Test Player1
        """
        model = kinow_client.models.player_1.Player1()


if __name__ == '__main__':
    unittest.main()
