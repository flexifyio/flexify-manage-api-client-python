# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1-dev
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class CostEstimateControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def estimate_migration_cost(self, migration_request, **kwargs):  # noqa: E501
        """estimateMigrationCost  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.estimate_migration_cost(migration_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddMigrationRequest migration_request: migrationRequest (required)
        :return: DtoMigrationCostEstimate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.estimate_migration_cost_with_http_info(migration_request, **kwargs)  # noqa: E501
        else:
            (data) = self.estimate_migration_cost_with_http_info(migration_request, **kwargs)  # noqa: E501
            return data

    def estimate_migration_cost_with_http_info(self, migration_request, **kwargs):  # noqa: E501
        """estimateMigrationCost  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.estimate_migration_cost_with_http_info(migration_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddMigrationRequest migration_request: migrationRequest (required)
        :return: DtoMigrationCostEstimate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method estimate_migration_cost" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_request' is set
        if ('migration_request' not in params or
                params['migration_request'] is None):
            raise ValueError("Missing the required parameter `migration_request` when calling `estimate_migration_cost`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'migration_request' in params:
            body_params = params['migration_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/cost/migration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoMigrationCostEstimate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
