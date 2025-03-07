# nexus-sdk
As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen
For more information, please visit [https://enterprise.atinary.com/documentation/#nexus](https://enterprise.atinary.com/documentation/#nexus).

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Atinary-technologies/nexus_sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Atinary-technologies/nexus_sdk.git`)

Then import the package:
```python
import nexus_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nexus_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.enterprise.atinary.com/nexus/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://api.enterprise.atinary.com/nexus/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.AdminApi(api_client)
    
    try:
        # Health check
        api_response = api_instance.health_check()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->health_check: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.enterprise.atinary.com/nexus/latest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**health_check**](docs/AdminApi.md#health_check) | **GET** /Healthcheck | Health check
*AdminApi* | [**service_information**](docs/AdminApi.md#service_information) | **GET** /ServiceInfo | Service information.
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /Files/{file_id} | Delete a file
*FilesApi* | [**delete_files**](docs/FilesApi.md#delete_files) | **POST** /Files/delete | 
*FilesApi* | [**download_file**](docs/FilesApi.md#download_file) | **GET** /Files/{file_id} | Download a file
*FilesApi* | [**list_files**](docs/FilesApi.md#list_files) | **GET** /Files | List available files for a project
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /Files | Upload a file under a project
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /Groups/{group_id} | Delete all projects in a group
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /Projects | Create a new project
*ProjectsApi* | [**create_tutorial_project**](docs/ProjectsApi.md#create_tutorial_project) | **POST** /Tutorial | Create the tutorial project
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /Projects/{project_id} | Delete a project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /Projects/{project_id} | Get project information
*ProjectsApi* | [**list_projects**](docs/ProjectsApi.md#list_projects) | **GET** /Projects | List project subscriptions
*ProjectsApi* | [**subscribe_users**](docs/ProjectsApi.md#subscribe_users) | **POST** /Projects/{project_id}/Subscribe | Add users to a project
*ProjectsApi* | [**unsubscribe**](docs/ProjectsApi.md#unsubscribe) | **POST** /Projects/{project_id}/Unsubscribe | Unsubscribe from a project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /Projects/{project_id} | Update project name, description and owner


## Documentation For Models

 - [AvailableFile](docs/AvailableFile.md)
 - [AvailableFilesSummary](docs/AvailableFilesSummary.md)
 - [AvailableProject](docs/AvailableProject.md)
 - [CreateProjectResponse](docs/CreateProjectResponse.md)
 - [DeleteFilesReq](docs/DeleteFilesReq.md)
 - [FileExtension](docs/FileExtension.md)
 - [GenericResponse](docs/GenericResponse.md)
 - [HealthCheckReport](docs/HealthCheckReport.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListProjectsResponse](docs/ListProjectsResponse.md)
 - [ProjectCreateReq](docs/ProjectCreateReq.md)
 - [ProjectDetail](docs/ProjectDetail.md)
 - [ProjectDetailResponse](docs/ProjectDetailResponse.md)
 - [ProjectSubscribeReq](docs/ProjectSubscribeReq.md)
 - [ProjectUnsubscribeReq](docs/ProjectUnsubscribeReq.md)
 - [ProjectUpdateReq](docs/ProjectUpdateReq.md)
 - [Result](docs/Result.md)
 - [ServiceInfo](docs/ServiceInfo.md)
 - [ServiceInfoResponse](docs/ServiceInfoResponse.md)
 - [UploadResponse](docs/UploadResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header

<a id="tokens"></a>
### tokens

- **Type**: Bearer authentication (JWT)


## Author

support@atinary.com


