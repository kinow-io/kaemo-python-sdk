# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.genders import Genders


class TestGenders(unittest.TestCase):
    """ Genders unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGenders(self):
        """
        Test Genders
        """
        model = kinow_client.models.genders.Genders()


if __name__ == '__main__':
    unittest.main()
