# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.64
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.features_api import FeaturesApi


class TestFeaturesApi(unittest.TestCase):
    """ FeaturesApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.features_api.FeaturesApi()

    def tearDown(self):
        pass

    def test_attach_features_to_product(self):
        """
        Test case for attach_features_to_product

        
        """
        pass

    def test_attach_features_to_video(self):
        """
        Test case for attach_features_to_video

        
        """
        pass

    def test_detach_feature_to_product(self):
        """
        Test case for detach_feature_to_product

        
        """
        pass

    def test_get_category_features(self):
        """
        Test case for get_category_features

        
        """
        pass

    def test_get_feature_values(self):
        """
        Test case for get_feature_values

        
        """
        pass

    def test_get_features(self):
        """
        Test case for get_features

        
        """
        pass

    def test_get_product_features(self):
        """
        Test case for get_product_features

        
        """
        pass

    def test_get_video_features(self):
        """
        Test case for get_video_features

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
