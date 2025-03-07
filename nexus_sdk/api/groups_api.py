# coding: utf-8

"""
    Atinary™ Nexus

    As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: support@atinary.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nexus_sdk.api_client import ApiClient
from nexus_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_group(self, group_id, **kwargs):  # noqa: E501
        """Delete all projects in a group  # noqa: E501

        Delete a Group. The group deletion causes the deletion of all projects, files, and subscriptions associated with it. Note that a group can only be deleted by an admin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Group identifiers (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GenericResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_group_with_http_info(group_id, **kwargs)  # noqa: E501

    def delete_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Delete all projects in a group  # noqa: E501

        Delete a Group. The group deletion causes the deletion of all projects, files, and subscriptions associated with it. Note that a group can only be deleted by an admin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Group identifiers (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GenericResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and local_var_params.get('group_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `delete_group`")  # noqa: E501

        if self.api_client.client_side_validation and ('group_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['group_id']) > 128):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `group_id` when calling `delete_group`, length must be less than or equal to `128`")  # noqa: E501
        if self.api_client.client_side_validation and ('group_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['group_id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `group_id` when calling `delete_group`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'group_id' in local_var_params and not re.search(r'^[\w-]+$', local_var_params['group_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `group_id` when calling `delete_group`, must conform to the pattern `/^[\w-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'tokens']  # noqa: E501

        response_types_map = {
            200: "GenericResponse",
            401: "GenericResponse",
            403: "GenericResponse",
        }

        return self.api_client.call_api(
            '/Groups/{group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
