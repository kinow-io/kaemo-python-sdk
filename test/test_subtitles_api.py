# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.subtitles_api import SubtitlesApi


class TestSubtitlesApi(unittest.TestCase):
    """ SubtitlesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.subtitles_api.SubtitlesApi()

    def tearDown(self):
        pass

    def test_get_subtitles(self):
        """
        Test case for get_subtitles

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
