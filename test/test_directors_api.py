# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.78
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.directors_api import DirectorsApi


class TestDirectorsApi(unittest.TestCase):
    """ DirectorsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.directors_api.DirectorsApi()

    def tearDown(self):
        pass

    def test_attach_product_to_director(self):
        """
        Test case for attach_product_to_director

        
        """
        pass

    def test_create_director(self):
        """
        Test case for create_director

        
        """
        pass

    def test_delete_director(self):
        """
        Test case for delete_director

        
        """
        pass

    def test_get_director(self):
        """
        Test case for get_director

        
        """
        pass

    def test_get_director_cover_image(self):
        """
        Test case for get_director_cover_image

        
        """
        pass

    def test_get_director_products(self):
        """
        Test case for get_director_products

        
        """
        pass

    def test_get_director_products_role(self):
        """
        Test case for get_director_products_role

        
        """
        pass

    def test_get_directors(self):
        """
        Test case for get_directors

        
        """
        pass

    def test_get_product_directors(self):
        """
        Test case for get_product_directors

        
        """
        pass

    def test_get_product_directors_role(self):
        """
        Test case for get_product_directors_role

        
        """
        pass

    def test_update_director(self):
        """
        Test case for update_director

        
        """
        pass

    def test_upload_director_cover(self):
        """
        Test case for upload_director_cover

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
