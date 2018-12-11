# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.64
    
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


class CartRulesApi(object):
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

    def attach_cart_rule_to_cart(self, cart_id, code, **kwargs):
        """
        Attach cart rule to cart
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_cart_rule_to_cart(cart_id, code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str code: Code of the cart rule to attach (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attach_cart_rule_to_cart_with_http_info(cart_id, code, **kwargs)
        else:
            (data) = self.attach_cart_rule_to_cart_with_http_info(cart_id, code, **kwargs)
            return data

    def attach_cart_rule_to_cart_with_http_info(self, cart_id, code, **kwargs):
        """
        Attach cart rule to cart
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_cart_rule_to_cart_with_http_info(cart_id, code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_id: Id of the cart to fetch (required)
        :param str code: Code of the cart rule to attach (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id', 'code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_cart_rule_to_cart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `attach_cart_rule_to_cart`")
        # verify the required parameter 'code' is set
        if ('code' not in params) or (params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `attach_cart_rule_to_cart`")


        collection_formats = {}

        resource_path = '/carts/{cart_id}/cart-rules'.replace('{format}', 'json')
        path_params = {}
        if 'cart_id' in params:
            path_params['cart_id'] = params['cart_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'code' in params:
            form_params.append(('code', params['code']))

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

    def create_cart_rule(self, body, **kwargs):
        """
        Create new cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_cart_rule(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CartRule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_cart_rule_with_http_info(body, **kwargs)
        else:
            (data) = self.create_cart_rule_with_http_info(body, **kwargs)
            return data

    def create_cart_rule_with_http_info(self, body, **kwargs):
        """
        Create new cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_cart_rule_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CartRule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cart_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_cart_rule`")


        collection_formats = {}

        resource_path = '/cart-rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        self.api_client.set_default_header('Content-Type', 'application/json')
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

    def delete_cart_rule(self, cart_rule_id, **kwargs):
        """
        Delete cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_cart_rule(cart_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_cart_rule_with_http_info(cart_rule_id, **kwargs)
        else:
            (data) = self.delete_cart_rule_with_http_info(cart_rule_id, **kwargs)
            return data

    def delete_cart_rule_with_http_info(self, cart_rule_id, **kwargs):
        """
        Delete cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_cart_rule_with_http_info(cart_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_rule_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cart_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_rule_id' is set
        if ('cart_rule_id' not in params) or (params['cart_rule_id'] is None):
            raise ValueError("Missing the required parameter `cart_rule_id` when calling `delete_cart_rule`")


        collection_formats = {}

        resource_path = '/cart-rules/{cart_rule_id}'.replace('{format}', 'json')
        path_params = {}
        if 'cart_rule_id' in params:
            path_params['cart_rule_id'] = params['cart_rule_id']

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

    def get_cart_rule(self, cart_rule_id, **kwargs):
        """
        Get cart rule by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart_rule(cart_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: ID of the cart rule to fetch (required)
        :return: CartRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_cart_rule_with_http_info(cart_rule_id, **kwargs)
        else:
            (data) = self.get_cart_rule_with_http_info(cart_rule_id, **kwargs)
            return data

    def get_cart_rule_with_http_info(self, cart_rule_id, **kwargs):
        """
        Get cart rule by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart_rule_with_http_info(cart_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: ID of the cart rule to fetch (required)
        :return: CartRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_rule_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cart_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_rule_id' is set
        if ('cart_rule_id' not in params) or (params['cart_rule_id'] is None):
            raise ValueError("Missing the required parameter `cart_rule_id` when calling `get_cart_rule`")


        collection_formats = {}

        resource_path = '/cart-rules/{cart_rule_id}'.replace('{format}', 'json')
        path_params = {}
        if 'cart_rule_id' in params:
            path_params['cart_rule_id'] = params['cart_rule_id']

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
                                        response_type='CartRule',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_cart_rules(self, **kwargs):
        """
        Get cart rules list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart_rules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: CartRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_cart_rules_with_http_info(**kwargs)
        else:
            (data) = self.get_cart_rules_with_http_info(**kwargs)
            return data

    def get_cart_rules_with_http_info(self, **kwargs):
        """
        Get cart rules list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart_rules_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: CartRules
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
                    " to method get_cart_rules" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/cart-rules'.replace('{format}', 'json')
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
                                        response_type='CartRules',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_cart_rule(self, cart_rule_id, body, **kwargs):
        """
        Update cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_cart_rule(cart_rule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: (required)
        :param CartRule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_cart_rule_with_http_info(cart_rule_id, body, **kwargs)
        else:
            (data) = self.update_cart_rule_with_http_info(cart_rule_id, body, **kwargs)
            return data

    def update_cart_rule_with_http_info(self, cart_rule_id, body, **kwargs):
        """
        Update cart rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_cart_rule_with_http_info(cart_rule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cart_rule_id: (required)
        :param CartRule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_rule_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_cart_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_rule_id' is set
        if ('cart_rule_id' not in params) or (params['cart_rule_id'] is None):
            raise ValueError("Missing the required parameter `cart_rule_id` when calling `update_cart_rule`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_cart_rule`")


        collection_formats = {}

        resource_path = '/cart-rules/{cart_rule_id}'.replace('{format}', 'json')
        path_params = {}
        if 'cart_rule_id' in params:
            path_params['cart_rule_id'] = params['cart_rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        self.api_client.set_default_header('Content-Type', 'application/json')
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
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
