# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.director_1 import Director1


class TestDirector1(unittest.TestCase):
    """ Director1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirector1(self):
        """
        Test Director1
        """
        model = kinow_client.models.director_1.Director1()


if __name__ == '__main__':
    unittest.main()
