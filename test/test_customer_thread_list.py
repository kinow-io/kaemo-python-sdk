# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.62
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_thread_list import CustomerThreadList


class TestCustomerThreadList(unittest.TestCase):
    """ CustomerThreadList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerThreadList(self):
        """
        Test CustomerThreadList
        """
        model = kinow_client.models.customer_thread_list.CustomerThreadList()


if __name__ == '__main__':
    unittest.main()
