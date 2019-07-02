# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.1.0
    
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


class AccessesApi(object):
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

    def get_available_category(self, category_id, **kwargs):
        """
        Get available category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_category(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: Category ID to fetch (required)
        :param int customer_id:
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_category_with_http_info(category_id, **kwargs)
        else:
            (data) = self.get_available_category_with_http_info(category_id, **kwargs)
            return data

    def get_available_category_with_http_info(self, category_id, **kwargs):
        """
        Get available category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_category_with_http_info(category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int category_id: Category ID to fetch (required)
        :param int customer_id:
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'customer_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_available_category`")


        collection_formats = {}

        resource_path = '/categories-accesses/{category_id}'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']

        query_params = {}
        if 'customer_id' in params:
            query_params['customer_id'] = params['customer_id']

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
                                        response_type='Category',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_has_access_to_product(self, customer_id, product_id, **kwargs):
        """
        Get customer access to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_has_access_to_product(customer_id, product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param int product_id: Product ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_has_access_to_product_with_http_info(customer_id, product_id, **kwargs)
        else:
            (data) = self.get_customer_has_access_to_product_with_http_info(customer_id, product_id, **kwargs)
            return data

    def get_customer_has_access_to_product_with_http_info(self, customer_id, product_id, **kwargs):
        """
        Get customer access to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_has_access_to_product_with_http_info(customer_id, product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param int product_id: Product ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'product_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_has_access_to_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_has_access_to_product`")
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_customer_has_access_to_product`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/products/{product_id}/has-access'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}

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
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_has_access_to_video(self, customer_id, video_id, **kwargs):
        """
        Get customer access to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_has_access_to_video(customer_id, video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param int video_id: Video ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_has_access_to_video_with_http_info(customer_id, video_id, **kwargs)
        else:
            (data) = self.get_customer_has_access_to_video_with_http_info(customer_id, video_id, **kwargs)
            return data

    def get_customer_has_access_to_video_with_http_info(self, customer_id, video_id, **kwargs):
        """
        Get customer access to video
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_has_access_to_video_with_http_info(customer_id, video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param int video_id: Video ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'video_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_has_access_to_video" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_has_access_to_video`")
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_customer_has_access_to_video`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/videos/{video_id}/has-access'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']

        query_params = {}

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
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_availability(self, product_id, **kwargs):
        """
        Get availability of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_availability(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_availability_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_availability_with_http_info(product_id, **kwargs)
            return data

    def get_product_availability_with_http_info(self, product_id, **kwargs):
        """
        Get availability of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_availability_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_availability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_availability`")


        collection_formats = {}

        resource_path = '/products/{product_id}/access'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}

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
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
