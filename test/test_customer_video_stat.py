# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.74
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_video_stat import CustomerVideoStat


class TestCustomerVideoStat(unittest.TestCase):
    """ CustomerVideoStat unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerVideoStat(self):
        """
        Test CustomerVideoStat
        """
        model = kinow_client.models.customer_video_stat.CustomerVideoStat()


if __name__ == '__main__':
    unittest.main()
