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
from kinow_client.models.payment_methods import PaymentMethods


class TestPaymentMethods(unittest.TestCase):
    """ PaymentMethods unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethods(self):
        """
        Test PaymentMethods
        """
        model = kinow_client.models.payment_methods.PaymentMethods()


if __name__ == '__main__':
    unittest.main()
