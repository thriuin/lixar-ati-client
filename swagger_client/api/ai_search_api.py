# coding: utf-8

"""
    ATIP AI Search API

    This API provides AI search functionalities: summary search and department recommendation.    Use the following code to authorize: ` nTsVPfUb89Ize/1DVSx2xKjLltOagND80lEfHaVB3fGT8CQEF7e9Lw== `  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: atip-support@lixar.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AISearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_get_combined_requestsget(self, search, **kwargs):  # noqa: E501
        """Summary search  # noqa: E501

        Returns a list of existing information request summaries and a list of deparments that would be able to provide infomration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_combined_requestsget(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for existing summaries or departments that relate to the search string (required)
        :param str organization: Filter results to the specified organization.
        :param int year: Filter results to the specified year.
        :param int month: Filter results to the specified month.
        :param int items_per_page: Determines how many items to include in one page.
        :param int page: Indicates which result page to display.
        :return: CombinedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_get_combined_requestsget_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.api_get_combined_requestsget_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def api_get_combined_requestsget_with_http_info(self, search, **kwargs):  # noqa: E501
        """Summary search  # noqa: E501

        Returns a list of existing information request summaries and a list of deparments that would be able to provide infomration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_combined_requestsget_with_http_info(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for existing summaries or departments that relate to the search string (required)
        :param str organization: Filter results to the specified organization.
        :param int year: Filter results to the specified year.
        :param int month: Filter results to the specified month.
        :param int items_per_page: Determines how many items to include in one page.
        :param int page: Indicates which result page to display.
        :return: CombinedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'organization', 'year', 'month', 'items_per_page', 'page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_get_combined_requestsget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `api_get_combined_requestsget`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'month' in params:
            query_params.append(('month', params['month']))  # noqa: E501
        if 'items_per_page' in params:
            query_params.append(('itemsPerPage', params['items_per_page']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/api/GetCombinedRequests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CombinedResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_get_departmentsget(self, search, **kwargs):  # noqa: E501
        """Department recommendation  # noqa: E501

        Returns a list of departmentes based on a search string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_departmentsget(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for departments that would know about this search string (required)
        :return: DepartmentRecommendationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_get_departmentsget_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.api_get_departmentsget_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def api_get_departmentsget_with_http_info(self, search, **kwargs):  # noqa: E501
        """Department recommendation  # noqa: E501

        Returns a list of departmentes based on a search string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_departmentsget_with_http_info(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for departments that would know about this search string (required)
        :return: DepartmentRecommendationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_get_departmentsget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `api_get_departmentsget`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/api/GetDepartments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DepartmentRecommendationResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_get_summariesget(self, search, **kwargs):  # noqa: E501
        """Summary search  # noqa: E501

        Returns a list of existing information request summaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_summariesget(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for existing summariesthat relate to the search string (required)
        :param str organization: Filter results to the specified organization.
        :param int year: Filter results to the specified year.
        :param int month: Filter results to the specified month.
        :param int items_per_page: Determines how many items to include in one page.
        :param int page: Indicates which result page to display.
        :return: SummarySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_get_summariesget_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.api_get_summariesget_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def api_get_summariesget_with_http_info(self, search, **kwargs):  # noqa: E501
        """Summary search  # noqa: E501

        Returns a list of existing information request summaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_get_summariesget_with_http_info(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Looking for existing summariesthat relate to the search string (required)
        :param str organization: Filter results to the specified organization.
        :param int year: Filter results to the specified year.
        :param int month: Filter results to the specified month.
        :param int items_per_page: Determines how many items to include in one page.
        :param int page: Indicates which result page to display.
        :return: SummarySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'organization', 'year', 'month', 'items_per_page', 'page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_get_summariesget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `api_get_summariesget`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'month' in params:
            query_params.append(('month', params['month']))  # noqa: E501
        if 'items_per_page' in params:
            query_params.append(('itemsPerPage', params['items_per_page']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/api/GetSummaries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SummarySearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)