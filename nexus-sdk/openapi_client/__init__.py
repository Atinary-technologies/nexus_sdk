# coding: utf-8

# flake8: noqa

"""
    Atinary™ Nexus

    As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).  # noqa: E501

    The version of the OpenAPI document: beta
    Contact: support@atinary.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.admin_api import AdminApi
from openapi_client.api.files_api import FilesApi
from openapi_client.api.projects_api import ProjectsApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.available_files_summary import AvailableFilesSummary
from openapi_client.models.create_project_response import CreateProjectResponse
from openapi_client.models.create_project_response_object import CreateProjectResponseObject
from openapi_client.models.generic_response import GenericResponse
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.list_files_response import ListFilesResponse
from openapi_client.models.list_files_response_objects import ListFilesResponseObjects
from openapi_client.models.list_projects_response import ListProjectsResponse
from openapi_client.models.list_projects_response_objects import ListProjectsResponseObjects
from openapi_client.models.project_create_req import ProjectCreateReq
from openapi_client.models.project_detail import ProjectDetail
from openapi_client.models.project_detail_response import ProjectDetailResponse
from openapi_client.models.project_subscribe_req import ProjectSubscribeReq
from openapi_client.models.project_unsubscribe_req import ProjectUnsubscribeReq
from openapi_client.models.project_update_req import ProjectUpdateReq
from openapi_client.models.result import Result
from openapi_client.models.service_info import ServiceInfo
from openapi_client.models.service_info_response import ServiceInfoResponse
from openapi_client.models.upload_response import UploadResponse
from openapi_client.models.upload_response_object import UploadResponseObject
