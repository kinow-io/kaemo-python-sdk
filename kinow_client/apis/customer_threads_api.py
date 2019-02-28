# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.74
    
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


class CustomerThreadsApi(object):
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

    def get_customer_thread(self, customer_thread_id, **kwargs):
        """
        Get customer thread
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_thread(customer_thread_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_thread_id: ID of the customer thread to fetch (required)
        :return: CustomerThread
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_thread_with_http_info(customer_thread_id, **kwargs)
        else:
            (data) = self.get_customer_thread_with_http_info(customer_thread_id, **kwargs)
            return data

    def get_customer_thread_with_http_info(self, customer_thread_id, **kwargs):
        """
        Get customer thread
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_thread_with_http_info(customer_thread_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_thread_id: ID of the customer thread to fetch (required)
        :return: CustomerThread
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_thread_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_thread" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_thread_id' is set
        if ('customer_thread_id' not in params) or (params['customer_thread_id'] is None):
            raise ValueError("Missing the required parameter `customer_thread_id` when calling `get_customer_thread`")


        collection_formats = {}

        resource_path = '/customer-threads/{customer_thread_id}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_thread_id' in params:
            path_params['customer_thread_id'] = params['customer_thread_id']

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
                                        response_type='CustomerThread',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_threads(self, **kwargs):
        """
        Get customer threads list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_threads(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str date_add:
        :param str date_add_operator:
        :return: CustomerThread1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_threads_with_http_info(**kwargs)
        else:
            (data) = self.get_customer_threads_with_http_info(**kwargs)
            return data

    def get_customer_threads_with_http_info(self, **kwargs):
        """
        Get customer threads list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_threads_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str date_add:
        :param str date_add_operator:
        :return: CustomerThread1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'date_add', 'date_add_operator']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_threads" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/customer-threads'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'date_add' in params:
            query_params['date_add'] = params['date_add']
        if 'date_add_operator' in params:
            query_params['date_add_operator'] = params['date_add_operator']

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
                                        response_type='CustomerThread1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
