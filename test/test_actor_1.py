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
from kinow_client.models.actor_1 import Actor1


class TestActor1(unittest.TestCase):
    """ Actor1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActor1(self):
        """
        Test Actor1
        """
        model = kinow_client.models.actor_1.Actor1()


if __name__ == '__main__':
    unittest.main()
