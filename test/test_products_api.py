# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.products_api import ProductsApi


class TestProductsApi(unittest.TestCase):
    """ ProductsApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.products_api.ProductsApi()

    def tearDown(self):
        pass

    def test_attach_features_to_product(self):
        """
        Test case for attach_features_to_product

        
        """
        pass

    def test_attach_product_to_category(self):
        """
        Test case for attach_product_to_category

        
        """
        pass

    def test_attach_video_to_product(self):
        """
        Test case for attach_video_to_product

        
        """
        pass

    def test_create_product(self):
        """
        Test case for create_product

        
        """
        pass

    def test_delete_product(self):
        """
        Test case for delete_product

        
        """
        pass

    def test_detach_feature_to_product(self):
        """
        Test case for detach_feature_to_product

        
        """
        pass

    def test_get_category_products(self):
        """
        Test case for get_category_products

        
        """
        pass

    def test_get_customer_has_access_to_product(self):
        """
        Test case for get_customer_has_access_to_product

        
        """
        pass

    def test_get_product(self):
        """
        Test case for get_product

        
        """
        pass

    def test_get_product_actors(self):
        """
        Test case for get_product_actors

        
        """
        pass

    def test_get_product_attributes(self):
        """
        Test case for get_product_attributes

        
        """
        pass

    def test_get_product_availability(self):
        """
        Test case for get_product_availability

        
        """
        pass

    def test_get_product_categories(self):
        """
        Test case for get_product_categories

        
        """
        pass

    def test_get_product_cover_image(self):
        """
        Test case for get_product_cover_image

        
        """
        pass

    def test_get_product_directors(self):
        """
        Test case for get_product_directors

        
        """
        pass

    def test_get_product_extracts(self):
        """
        Test case for get_product_extracts

        
        """
        pass

    def test_get_product_features(self):
        """
        Test case for get_product_features

        
        """
        pass

    def test_get_product_geolocations(self):
        """
        Test case for get_product_geolocations

        
        """
        pass

    def test_get_product_geolocations_by_ip(self):
        """
        Test case for get_product_geolocations_by_ip

        
        """
        pass

    def test_get_product_images(self):
        """
        Test case for get_product_images

        
        """
        pass

    def test_get_products(self):
        """
        Test case for get_products

        
        """
        pass

    def test_get_videos_from_product(self):
        """
        Test case for get_videos_from_product

        
        """
        pass

    def test_search_products(self):
        """
        Test case for search_products

        
        """
        pass

    def test_set_product_geolocation(self):
        """
        Test case for set_product_geolocation

        
        """
        pass

    def test_update_product(self):
        """
        Test case for update_product

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
