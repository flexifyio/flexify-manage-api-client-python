# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.6
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class MigrationsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_migration(self, migration_request, **kwargs):  # noqa: E501
        """Add new migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_migration(migration_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param AddMigrationRequest migration_request: migrationRequest (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_migration_with_http_info(migration_request, **kwargs)  # noqa: E501
        else:
            (data) = self.add_migration_with_http_info(migration_request, **kwargs)  # noqa: E501
            return data

    def add_migration_with_http_info(self, migration_request, **kwargs):  # noqa: E501
        """Add new migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_migration_with_http_info(migration_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param AddMigrationRequest migration_request: migrationRequest (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_migration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_request' is set
        if ('migration_request' not in params or
                params['migration_request'] is None):
            raise ValueError("Missing the required parameter `migration_request` when calling `add_migration`")  # noqa: E501

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
            '/rest/migrations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migration(self, migration_id, **kwargs):  # noqa: E501
        """Get migration by id. Only migration owner or administrator have access to the migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_migration(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: Migration Id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
            return data

    def get_migration_with_http_info(self, migration_id, **kwargs):  # noqa: E501
        """Get migration by id. Only migration owner or administrator have access to the migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_migration_with_http_info(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: Migration Id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_id' is set
        if ('migration_id' not in params or
                params['migration_id'] is None):
            raise ValueError("Missing the required parameter `migration_id` when calling `get_migration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'migration_id' in params:
            path_params['migration-id'] = params['migration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/migrations/{migration-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Migration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migrations(self, **kwargs):  # noqa: E501
        """Get all migrations for logged in user in pagged mode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_migrations(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_hidden: Include hidden migrations to response
        :param list[str] sort: Attributes to sort
        :param int page: Page number
        :param int size: Page size
        :param str sort_direction: Sort Direction
        :return: PageMigration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_migrations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_migrations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_migrations_with_http_info(self, **kwargs):  # noqa: E501
        """Get all migrations for logged in user in pagged mode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_migrations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_hidden: Include hidden migrations to response
        :param list[str] sort: Attributes to sort
        :param int page: Page number
        :param int size: Page size
        :param str sort_direction: Sort Direction
        :return: PageMigration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_hidden', 'sort', 'page', 'size', 'sort_direction']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migrations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_hidden' in params:
            query_params.append(('include-hidden', params['include_hidden']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/migrations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageMigration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hide_migration(self, migration_id, **kwargs):  # noqa: E501
        """Hide migration from UI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.hide_migration(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: migration-id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.hide_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.hide_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
            return data

    def hide_migration_with_http_info(self, migration_id, **kwargs):  # noqa: E501
        """Hide migration from UI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.hide_migration_with_http_info(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: migration-id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hide_migration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_id' is set
        if ('migration_id' not in params or
                params['migration_id'] is None):
            raise ValueError("Missing the required parameter `migration_id` when calling `hide_migration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'migration_id' in params:
            path_params['migration-id'] = params['migration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/migrations/{migration-id}/hide', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Migration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stop_migration(self, migration_id, **kwargs):  # noqa: E501
        """Stop (cancel) the migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.stop_migration(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: migration-id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.stop_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stop_migration_with_http_info(migration_id, **kwargs)  # noqa: E501
            return data

    def stop_migration_with_http_info(self, migration_id, **kwargs):  # noqa: E501
        """Stop (cancel) the migration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.stop_migration_with_http_info(migration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int migration_id: migration-id (required)
        :return: Migration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_migration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_id' is set
        if ('migration_id' not in params or
                params['migration_id'] is None):
            raise ValueError("Missing the required parameter `migration_id` when calling `stop_migration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'migration_id' in params:
            path_params['migration-id'] = params['migration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/migrations/{migration-id}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Migration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
