# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.73
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.session_video_stats import SessionVideoStats


class TestSessionVideoStats(unittest.TestCase):
    """ SessionVideoStats unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSessionVideoStats(self):
        """
        Test SessionVideoStats
        """
        model = kinow_client.models.session_video_stats.SessionVideoStats()


if __name__ == '__main__':
    unittest.main()
