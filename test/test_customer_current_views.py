# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.43
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.customer_current_views import CustomerCurrentViews


class TestCustomerCurrentViews(unittest.TestCase):
    """ CustomerCurrentViews unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerCurrentViews(self):
        """
        Test CustomerCurrentViews
        """
        model = kaemo_client.models.customer_current_views.CustomerCurrentViews()


if __name__ == '__main__':
    unittest.main()
