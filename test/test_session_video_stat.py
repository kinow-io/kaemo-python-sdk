# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.65
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.session_video_stat import SessionVideoStat


class TestSessionVideoStat(unittest.TestCase):
    """ SessionVideoStat unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSessionVideoStat(self):
        """
        Test SessionVideoStat
        """
        model = kaemo_client.models.session_video_stat.SessionVideoStat()


if __name__ == '__main__':
    unittest.main()
