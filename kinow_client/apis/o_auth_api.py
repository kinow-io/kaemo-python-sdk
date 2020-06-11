# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.73
    
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


class OAuthApi(object):
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

    def get_token(self, client_id, client_secret, **kwargs):
        """
        Get authentication token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_token(client_id, client_secret, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_id: Client Id given by your back office (required)
        :param str client_secret: Client secret given by your back office (required)
        :return: OAuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_token_with_http_info(client_id, client_secret, **kwargs)
        else:
            (data) = self.get_token_with_http_info(client_id, client_secret, **kwargs)
            return data

    def get_token_with_http_info(self, client_id, client_secret, **kwargs):
        """
        Get authentication token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_token_with_http_info(client_id, client_secret, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_id: Client Id given by your back office (required)
        :param str client_secret: Client secret given by your back office (required)
        :return: OAuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'client_secret']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `get_token`")
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params) or (params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `get_token`")


        collection_formats = {}

        resource_path = '/get-token'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))

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
                                        response_type='OAuthToken',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
