# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.payment_module import PaymentModule


class TestPaymentModule(unittest.TestCase):
    """ PaymentModule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentModule(self):
        """
        Test PaymentModule
        """
        model = kinow_client.models.payment_module.PaymentModule()


if __name__ == '__main__':
    unittest.main()
