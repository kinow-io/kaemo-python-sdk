# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.81
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.page_lists import PageLists


class TestPageLists(unittest.TestCase):
    """ PageLists unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageLists(self):
        """
        Test PageLists
        """
        model = kinow_client.models.page_lists.PageLists()


if __name__ == '__main__':
    unittest.main()
