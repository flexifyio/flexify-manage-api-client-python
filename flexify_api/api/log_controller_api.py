# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.7-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class LogControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_log_for_current_user(self, page, size, **kwargs):  # noqa: E501
        """getLogForCurrentUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_log_for_current_user(page, size, async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number (required)
        :param int size: Page size (required)
        :param int endpoint_id: endpoint-id
        :param int migration_id: migration-id
        :param list[str] sort: Attributes to sort
        :param str sort_direction: Sort Direction
        :param int spring_page_request_offset:
        :param int spring_page_request_page_number:
        :param int spring_page_request_page_size:
        :param bool spring_page_request_paged:
        :param bool spring_page_request_sort_sorted:
        :param bool spring_page_request_sort_unsorted:
        :param bool spring_page_request_unpaged:
        :param int storage_id: storage-id
        :return: PageLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_log_for_current_user_with_http_info(page, size, **kwargs)  # noqa: E501
        else:
            (data) = self.get_log_for_current_user_with_http_info(page, size, **kwargs)  # noqa: E501
            return data

    def get_log_for_current_user_with_http_info(self, page, size, **kwargs):  # noqa: E501
        """getLogForCurrentUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_log_for_current_user_with_http_info(page, size, async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number (required)
        :param int size: Page size (required)
        :param int endpoint_id: endpoint-id
        :param int migration_id: migration-id
        :param list[str] sort: Attributes to sort
        :param str sort_direction: Sort Direction
        :param int spring_page_request_offset:
        :param int spring_page_request_page_number:
        :param int spring_page_request_page_size:
        :param bool spring_page_request_paged:
        :param bool spring_page_request_sort_sorted:
        :param bool spring_page_request_sort_unsorted:
        :param bool spring_page_request_unpaged:
        :param int storage_id: storage-id
        :return: PageLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'endpoint_id', 'migration_id', 'sort', 'sort_direction', 'spring_page_request_offset', 'spring_page_request_page_number', 'spring_page_request_page_size', 'spring_page_request_paged', 'spring_page_request_sort_sorted', 'spring_page_request_sort_unsorted', 'spring_page_request_unpaged', 'storage_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_log_for_current_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_log_for_current_user`")  # noqa: E501
        # verify the required parameter 'size' is set
        if ('size' not in params or
                params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `get_log_for_current_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_id' in params:
            query_params.append(('endpoint-id', params['endpoint_id']))  # noqa: E501
        if 'migration_id' in params:
            query_params.append(('migration-id', params['migration_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))  # noqa: E501
        if 'spring_page_request_offset' in params:
            query_params.append(('springPageRequest.offset', params['spring_page_request_offset']))  # noqa: E501
        if 'spring_page_request_page_number' in params:
            query_params.append(('springPageRequest.pageNumber', params['spring_page_request_page_number']))  # noqa: E501
        if 'spring_page_request_page_size' in params:
            query_params.append(('springPageRequest.pageSize', params['spring_page_request_page_size']))  # noqa: E501
        if 'spring_page_request_paged' in params:
            query_params.append(('springPageRequest.paged', params['spring_page_request_paged']))  # noqa: E501
        if 'spring_page_request_sort_sorted' in params:
            query_params.append(('springPageRequest.sort.sorted', params['spring_page_request_sort_sorted']))  # noqa: E501
        if 'spring_page_request_sort_unsorted' in params:
            query_params.append(('springPageRequest.sort.unsorted', params['spring_page_request_sort_unsorted']))  # noqa: E501
        if 'spring_page_request_unpaged' in params:
            query_params.append(('springPageRequest.unpaged', params['spring_page_request_unpaged']))  # noqa: E501
        if 'storage_id' in params:
            query_params.append(('storage-id', params['storage_id']))  # noqa: E501

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
            '/rest/log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageLogEntry',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
