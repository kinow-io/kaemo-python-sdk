# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.79
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_file import MediaFile


class TestMediaFile(unittest.TestCase):
    """ MediaFile unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaFile(self):
        """
        Test MediaFile
        """
        model = kinow_client.models.media_file.MediaFile()


if __name__ == '__main__':
    unittest.main()
