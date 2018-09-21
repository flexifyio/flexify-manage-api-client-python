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


class EndpointsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def attach_storages_to_endpoint(self, endpoint_id, request, **kwargs):  # noqa: E501
        """Attach the storage to the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.attach_storages_to_endpoint(endpoint_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param AttachStoragesToEndpointRequest request: request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.attach_storages_to_endpoint_with_http_info(endpoint_id, request, **kwargs)  # noqa: E501
        else:
            (data) = self.attach_storages_to_endpoint_with_http_info(endpoint_id, request, **kwargs)  # noqa: E501
            return data

    def attach_storages_to_endpoint_with_http_info(self, endpoint_id, request, **kwargs):  # noqa: E501
        """Attach the storage to the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.attach_storages_to_endpoint_with_http_info(endpoint_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param AttachStoragesToEndpointRequest request: request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_storages_to_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `attach_storages_to_endpoint`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `attach_storages_to_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/endpoints/{endpoint-id}/storages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def detach_storage_from_endpoint(self, endpoint_id, storage_id, **kwargs):  # noqa: E501
        """Detach the storage from the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.detach_storage_from_endpoint(endpoint_id, storage_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param int storage_id: storage-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.detach_storage_from_endpoint_with_http_info(endpoint_id, storage_id, **kwargs)  # noqa: E501
        else:
            (data) = self.detach_storage_from_endpoint_with_http_info(endpoint_id, storage_id, **kwargs)  # noqa: E501
            return data

    def detach_storage_from_endpoint_with_http_info(self, endpoint_id, storage_id, **kwargs):  # noqa: E501
        """Detach the storage from the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.detach_storage_from_endpoint_with_http_info(endpoint_id, storage_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param int storage_id: storage-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'storage_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detach_storage_from_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `detach_storage_from_endpoint`")  # noqa: E501
        # verify the required parameter 'storage_id' is set
        if ('storage_id' not in params or
                params['storage_id'] is None):
            raise ValueError("Missing the required parameter `storage_id` when calling `detach_storage_from_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501
        if 'storage_id' in params:
            path_params['storage-id'] = params['storage_id']  # noqa: E501

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
            '/rest/endpoints/{endpoint-id}/storages/{storage-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disable(self, endpoint_id, **kwargs):  # noqa: E501
        """Disable the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.disable_with_http_info(endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.disable_with_http_info(endpoint_id, **kwargs)  # noqa: E501
            return data

    def disable_with_http_info(self, endpoint_id, **kwargs):  # noqa: E501
        """Disable the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable_with_http_info(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `disable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

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
            '/rest/endpoints/{endpoint-id}/actions/disable', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable(self, endpoint_id, **kwargs):  # noqa: E501
        """Enable the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.enable_with_http_info(endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_with_http_info(endpoint_id, **kwargs)  # noqa: E501
            return data

    def enable_with_http_info(self, endpoint_id, **kwargs):  # noqa: E501
        """Enable the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.enable_with_http_info(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `enable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

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
            '/rest/endpoints/{endpoint-id}/actions/enable', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_endpoint_details(self, endpoint_id, **kwargs):  # noqa: E501
        """Get endpoint details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_endpoint_details(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: EndpointDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_endpoint_details_with_http_info(endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_endpoint_details_with_http_info(endpoint_id, **kwargs)  # noqa: E501
            return data

    def get_endpoint_details_with_http_info(self, endpoint_id, **kwargs):  # noqa: E501
        """Get endpoint details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_endpoint_details_with_http_info(endpoint_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :return: EndpointDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_endpoint_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `get_endpoint_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

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
            '/rest/endpoints/{endpoint-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EndpointDetails',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_endpoints_for_current_user(self, **kwargs):  # noqa: E501
        """Get endpoint for current user. This method will create new endpoint if no endpoints exist for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_endpoints_for_current_user(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[EndpointDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_endpoints_for_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_endpoints_for_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_endpoints_for_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get endpoint for current user. This method will create new endpoint if no endpoints exist for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_endpoints_for_current_user_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[EndpointDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_endpoints_for_current_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/rest/endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EndpointDetails]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_storage_put_objects(self, endpoint_id, storage_id, settings, **kwargs):  # noqa: E501
        """Set given storage as default for the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_storage_put_objects(endpoint_id, storage_id, settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param int storage_id: storage-id (required)
        :param EndpointStorageSettings settings: settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_storage_put_objects_with_http_info(endpoint_id, storage_id, settings, **kwargs)  # noqa: E501
        else:
            (data) = self.set_storage_put_objects_with_http_info(endpoint_id, storage_id, settings, **kwargs)  # noqa: E501
            return data

    def set_storage_put_objects_with_http_info(self, endpoint_id, storage_id, settings, **kwargs):  # noqa: E501
        """Set given storage as default for the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_storage_put_objects_with_http_info(endpoint_id, storage_id, settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param int storage_id: storage-id (required)
        :param EndpointStorageSettings settings: settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'storage_id', 'settings']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_storage_put_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `set_storage_put_objects`")  # noqa: E501
        # verify the required parameter 'storage_id' is set
        if ('storage_id' not in params or
                params['storage_id'] is None):
            raise ValueError("Missing the required parameter `storage_id` when calling `set_storage_put_objects`")  # noqa: E501
        # verify the required parameter 'settings' is set
        if ('settings' not in params or
                params['settings'] is None):
            raise ValueError("Missing the required parameter `settings` when calling `set_storage_put_objects`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501
        if 'storage_id' in params:
            path_params['storage-id'] = params['storage_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings' in params:
            body_params = params['settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/endpoints/{endpoint-id}/storages/{storage-id}/put-objects', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_endpoint(self, endpoint_id, endpoint, **kwargs):  # noqa: E501
        """Update attributes of the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_endpoint(endpoint_id, endpoint, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param Endpoint endpoint: endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_endpoint_with_http_info(endpoint_id, endpoint, **kwargs)  # noqa: E501
        else:
            (data) = self.update_endpoint_with_http_info(endpoint_id, endpoint, **kwargs)  # noqa: E501
            return data

    def update_endpoint_with_http_info(self, endpoint_id, endpoint, **kwargs):  # noqa: E501
        """Update attributes of the endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_endpoint_with_http_info(endpoint_id, endpoint, async=True)
        >>> result = thread.get()

        :param async bool
        :param int endpoint_id: endpoint-id (required)
        :param Endpoint endpoint: endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'endpoint']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `update_endpoint`")  # noqa: E501
        # verify the required parameter 'endpoint' is set
        if ('endpoint' not in params or
                params['endpoint'] is None):
            raise ValueError("Missing the required parameter `endpoint` when calling `update_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'endpoint' in params:
            body_params = params['endpoint']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/endpoints/{endpoint-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
