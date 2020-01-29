# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FeaturesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def attach_features_to_product(self, product_id, features, **kwargs):
        """
        Attach feature to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_features_to_product(product_id, features, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: (required)
        :param str features:       To attach existing FeatureValue to Product:      ```      [{      \"id_feature\":3,      \"id_feature_value\":5      }]```        To create a custom FeatureValue:      ```      [{      \"id_feature\":3,      \"custom_value\":[{      \"lang\": 1,      \"value\": \"string\"      }]      }]``` (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attach_features_to_product_with_http_info(product_id, features, **kwargs)
        else:
            (data) = self.attach_features_to_product_with_http_info(product_id, features, **kwargs)
            return data

    def attach_features_to_product_with_http_info(self, product_id, features, **kwargs):
        """
        Attach feature to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_features_to_product_with_http_info(product_id, features, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: (required)
        :param str features:       To attach existing FeatureValue to Product:      ```      [{      \"id_feature\":3,      \"id_feature_value\":5      }]```        To create a custom FeatureValue:      ```      [{      \"id_feature\":3,      \"custom_value\":[{      \"lang\": 1,      \"value\": \"string\"      }]      }]``` (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'features']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_features_to_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `attach_features_to_product`")
        # verify the required parameter 'features' is set
        if ('features' not in params) or (params['features'] is None):
            raise ValueError("Missing the required parameter `features` when calling `attach_features_to_product`")


        collection_formats = {}

        resource_path = '/products/{product_id}/features'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'features' in params:
            form_params.append(('features', params['features']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attach_features_to_video(self, video_id, features, **kwargs):
        """
        Attach feature to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_features_to_video(video_id, features, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: (required)
        :param str features:       To attach existing FeatureValue to Product:      ```      [{      \"id_feature\":3,      \"id_feature_value\":5      }]      ```        To create a custom FeatureValue:      ```      [{      \"id_feature\":3,      \"custom_value\":[{      \"lang\": 1,      \"value\": \"string\"      }]      }]      ``` (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attach_features_to_video_with_http_info(video_id, features, **kwargs)
        else:
            (data) = self.attach_features_to_video_with_http_info(video_id, features, **kwargs)
            return data

    def attach_features_to_video_with_http_info(self, video_id, features, **kwargs):
        """
        Attach feature to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_features_to_video_with_http_info(video_id, features, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: (required)
        :param str features:       To attach existing FeatureValue to Product:      ```      [{      \"id_feature\":3,      \"id_feature_value\":5      }]      ```        To create a custom FeatureValue:      ```      [{      \"id_feature\":3,      \"custom_value\":[{      \"lang\": 1,      \"value\": \"string\"      }]      }]      ``` (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'features']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_features_to_video" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `attach_features_to_video`")
        # verify the required parameter 'features' is set
        if ('features' not in params) or (params['features'] is None):
            raise ValueError("Missing the required parameter `features` when calling `attach_features_to_video`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/features'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'features' in params:
            form_params.append(('features', params['features']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def detach_feature_to_product(self, product_id, feature_id, **kwargs):
        """
        Detach feature to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.detach_feature_to_product(product_id, feature_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: (required)
        :param int feature_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.detach_feature_to_product_with_http_info(product_id, feature_id, **kwargs)
        else:
            (data) = self.detach_feature_to_product_with_http_info(product_id, feature_id, **kwargs)
            return data

    def detach_feature_to_product_with_http_info(self, product_id, feature_id, **kwargs):
        """
        Detach feature to product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.detach_feature_to_product_with_http_info(product_id, feature_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: (required)
        :param int feature_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'feature_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detach_feature_to_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `detach_feature_to_product`")
        # verify the required parameter 'feature_id' is set
        if ('feature_id' not in params) or (params['feature_id'] is None):
            raise ValueError("Missing the required parameter `feature_id` when calling `detach_feature_to_product`")


        collection_formats = {}

        resource_path = '/products/{product_id}/features/{feature_id}'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']
        if 'feature_id' in params:
            path_params['feature_id'] = params['feature_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_category_features(self, category_id, **kwargs):
        """
        Get category features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_category_features(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: Category ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_category_features_with_http_info(category_id, **kwargs)
        else:
            (data) = self.get_category_features_with_http_info(category_id, **kwargs)
            return data

    def get_category_features_with_http_info(self, category_id, **kwargs):
        """
        Get category features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_category_features_with_http_info(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: Category ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_category_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_category_features`")


        collection_formats = {}

        resource_path = '/categories/{category_id}/features'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Features',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_feature_values(self, **kwargs):
        """
        Get feature value list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_feature_values(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Products1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_feature_values_with_http_info(**kwargs)
        else:
            (data) = self.get_feature_values_with_http_info(**kwargs)
            return data

    def get_feature_values_with_http_info(self, **kwargs):
        """
        Get feature value list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_feature_values_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Products1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_values" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/feature-values'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Products1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_features(self, **kwargs):
        """
        Get feature list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_features(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_features_with_http_info(**kwargs)
        else:
            (data) = self.get_features_with_http_info(**kwargs)
            return data

    def get_features_with_http_info(self, **kwargs):
        """
        Get feature list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_features_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_features" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/features'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Features',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_features(self, product_id, **kwargs):
        """
        Get product features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_features(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_features_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_features_with_http_info(product_id, **kwargs)
            return data

    def get_product_features_with_http_info(self, product_id, **kwargs):
        """
        Get product features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_features_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_features`")


        collection_formats = {}

        resource_path = '/products/{product_id}/features'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Features',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_video_features(self, video_id, **kwargs):
        """
        Get video features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_features(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_features_with_http_info(video_id, **kwargs)
        else:
            (data) = self.get_video_features_with_http_info(video_id, **kwargs)
            return data

    def get_video_features_with_http_info(self, video_id, **kwargs):
        """
        Get video features
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_features_with_http_info(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_features`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/features'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Features',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
