# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.bookmarks_api import BookmarksApi


class TestBookmarksApi(unittest.TestCase):
    """ BookmarksApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.bookmarks_api.BookmarksApi()

    def tearDown(self):
        pass

    def test_attach_bookmark_to_customer(self):
        """
        Test case for attach_bookmark_to_customer

        
        """
        pass

    def test_detach_bookmark_from_customer(self):
        """
        Test case for detach_bookmark_from_customer

        
        """
        pass

    def test_get_customer_bookmarks(self):
        """
        Test case for get_customer_bookmarks

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
