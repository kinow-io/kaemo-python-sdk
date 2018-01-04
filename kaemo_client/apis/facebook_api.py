# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.35
    
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


class FacebookApi(object):
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

    def create_facebook_id(self, customer_id, facebook_id, **kwargs):
        """
        Create new Facebook ID for user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_facebook_id(customer_id, facebook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID (required)
        :param str facebook_id: Facebook ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_facebook_id_with_http_info(customer_id, facebook_id, **kwargs)
        else:
            (data) = self.create_facebook_id_with_http_info(customer_id, facebook_id, **kwargs)
            return data

    def create_facebook_id_with_http_info(self, customer_id, facebook_id, **kwargs):
        """
        Create new Facebook ID for user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_facebook_id_with_http_info(customer_id, facebook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID (required)
        :param str facebook_id: Facebook ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'facebook_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_facebook_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `create_facebook_id`")
        # verify the required parameter 'facebook_id' is set
        if ('facebook_id' not in params) or (params['facebook_id'] is None):
            raise ValueError("Missing the required parameter `facebook_id` when calling `create_facebook_id`")


        collection_formats = {}

        resource_path = '/facebook/customers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'customer_id' in params:
            form_params.append(('customer_id', params['customer_id']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'facebook_id' in params:
            form_params.append(('facebook_id', params['facebook_id']))

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

    def get_facebook_customer(self, facebook_id, **kwargs):
        """
        Get customer ID by Facebook ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_facebook_customer(facebook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facebook_id: Facebook ID to fetch (required)
        :return: CustomerId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_facebook_customer_with_http_info(facebook_id, **kwargs)
        else:
            (data) = self.get_facebook_customer_with_http_info(facebook_id, **kwargs)
            return data

    def get_facebook_customer_with_http_info(self, facebook_id, **kwargs):
        """
        Get customer ID by Facebook ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_facebook_customer_with_http_info(facebook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facebook_id: Facebook ID to fetch (required)
        :return: CustomerId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facebook_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facebook_customer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facebook_id' is set
        if ('facebook_id' not in params) or (params['facebook_id'] is None):
            raise ValueError("Missing the required parameter `facebook_id` when calling `get_facebook_customer`")


        collection_formats = {}

        resource_path = '/facebook/customers/{facebook_id}'.replace('{format}', 'json')
        path_params = {}
        if 'facebook_id' in params:
            path_params['facebook_id'] = params['facebook_id']

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
                                        response_type='CustomerId',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
