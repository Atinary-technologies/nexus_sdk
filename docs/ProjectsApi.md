# nexus_sdk.ProjectsApi

All URIs are relative to *https://scientia.atinary.com/nexus/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /Projects | Create a new project
[**create_tutorial_project**](ProjectsApi.md#create_tutorial_project) | **POST** /Tutorial | Create the tutorial project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /Projects/{project_id} | Delete a project
[**get_project**](ProjectsApi.md#get_project) | **GET** /Projects/{project_id} | Get project information
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /Projects | List project subscriptions
[**subscribe_users**](ProjectsApi.md#subscribe_users) | **POST** /Projects/{project_id}/Subscribe | Add users to a project
[**unsubscribe**](ProjectsApi.md#unsubscribe) | **POST** /Projects/{project_id}/Unsubscribe | Unsubscribe from a project
[**update_project**](ProjectsApi.md#update_project) | **PUT** /Projects/{project_id} | Update project name, description and owner


# **create_project**
> CreateProjectResponse create_project(project_create_req=project_create_req)

Create a new project

Create a new project by providing a project name. The user who calls this method is automatically added to the project and assigned as **project owner**. Note that if the user is already subscribed to a project with the same name the request will be denied.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_create_req = nexus_sdk.ProjectCreateReq() # ProjectCreateReq | Json object specifying the **name**. (optional)

    try:
        # Create a new project
        api_response = api_instance.create_project(project_create_req=project_create_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_create_req = nexus_sdk.ProjectCreateReq() # ProjectCreateReq | Json object specifying the **name**. (optional)

    try:
        # Create a new project
        api_response = api_instance.create_project(project_create_req=project_create_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_req** | [**ProjectCreateReq**](ProjectCreateReq.md)| Json object specifying the **name**. | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project successfully created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tutorial_project**
> CreateProjectResponse create_tutorial_project(group_id=group_id)

Create the tutorial project

Create an example project containing a text file with some basic instructions on it.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers (optional)

    try:
        # Create the tutorial project
        api_response = api_instance.create_tutorial_project(group_id=group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_tutorial_project: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers (optional)

    try:
        # Create the tutorial project
        api_response = api_instance.create_tutorial_project(group_id=group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_tutorial_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group identifiers | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tutorial Project successfully created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> GenericResponse delete_project(project_id)

Delete a project

Delete a project. The project deletion causes the deletion of all files and subscriptions associated with it. Note that a project can only be deleted by the **project owner**.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.

    try:
        # Delete a project
        api_response = api_instance.delete_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.

    try:
        # Delete a project
        api_response = api_instance.delete_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project successfully deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectDetailResponse get_project(project_id)

Get project information

Get project information. List project id, project owner, members and creation date. Note that only users subscribed to the project can request for information on it.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.

    try:
        # Get project information
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.

    try:
        # Get project information
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 

### Return type

[**ProjectDetailResponse**](ProjectDetailResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project successfully retrieved |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjectsResponse list_projects(group_id=group_id)

List project subscriptions

List individual project subscriptions.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers (optional)

    try:
        # List project subscriptions
        api_response = api_instance.list_projects(group_id=group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers (optional)

    try:
        # List project subscriptions
        api_response = api_instance.list_projects(group_id=group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group identifiers | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List successfully retrieved |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_users**
> ProjectDetailResponse subscribe_users(project_id, project_subscribe_req=project_subscribe_req)

Add users to a project

Add users to a project. Note that only the **project owner** can add users to the project.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_subscribe_req = nexus_sdk.ProjectSubscribeReq() # ProjectSubscribeReq | Json object containing the list of user **emails** to add to the project. (optional)

    try:
        # Add users to a project
        api_response = api_instance.subscribe_users(project_id, project_subscribe_req=project_subscribe_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->subscribe_users: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_subscribe_req = nexus_sdk.ProjectSubscribeReq() # ProjectSubscribeReq | Json object containing the list of user **emails** to add to the project. (optional)

    try:
        # Add users to a project
        api_response = api_instance.subscribe_users(project_id, project_subscribe_req=project_subscribe_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->subscribe_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 
 **project_subscribe_req** | [**ProjectSubscribeReq**](ProjectSubscribeReq.md)| Json object containing the list of user **emails** to add to the project. | [optional] 

### Return type

[**ProjectDetailResponse**](ProjectDetailResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users successfully invited to join project |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe**
> ProjectDetailResponse unsubscribe(project_id, project_unsubscribe_req=project_unsubscribe_req)

Unsubscribe from a project

Unsubscribe oneself from a project or unsubscribe members from a project. Note that: 1) to unsubscribe members from a project one needs to be **project owner**, and 2) the **project owner** can not unsubscribe from his own project.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_unsubscribe_req = nexus_sdk.ProjectUnsubscribeReq() # ProjectUnsubscribeReq | Json object containing the list of user **emails** to unsubscribe from the project. If this list is empty, then the caller is unsubscribed from the project. (optional)

    try:
        # Unsubscribe from a project
        api_response = api_instance.unsubscribe(project_id, project_unsubscribe_req=project_unsubscribe_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->unsubscribe: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_unsubscribe_req = nexus_sdk.ProjectUnsubscribeReq() # ProjectUnsubscribeReq | Json object containing the list of user **emails** to unsubscribe from the project. If this list is empty, then the caller is unsubscribed from the project. (optional)

    try:
        # Unsubscribe from a project
        api_response = api_instance.unsubscribe(project_id, project_unsubscribe_req=project_unsubscribe_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 
 **project_unsubscribe_req** | [**ProjectUnsubscribeReq**](ProjectUnsubscribeReq.md)| Json object containing the list of user **emails** to unsubscribe from the project. If this list is empty, then the caller is unsubscribed from the project. | [optional] 

### Return type

[**ProjectDetailResponse**](ProjectDetailResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription from project successfully deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> CreateProjectResponse update_project(project_id, project_update_req=project_update_req)

Update project name, description and owner

Update project name, description and owner

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_update_req = nexus_sdk.ProjectUpdateReq() # ProjectUpdateReq | Json object containing  **new_name**, **new_description** and/or **new_owner**. Note that only users subscribed to the project can be project owners. The project owner is the only one authorized to call this method. (optional)

    try:
        # Update project name, description and owner
        api_response = api_instance.update_project(project_id, project_update_req=project_update_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus_sdk
from nexus_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest"
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
    api_instance = nexus_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
project_update_req = nexus_sdk.ProjectUpdateReq() # ProjectUpdateReq | Json object containing  **new_name**, **new_description** and/or **new_owner**. Note that only users subscribed to the project can be project owners. The project owner is the only one authorized to call this method. (optional)

    try:
        # Update project name, description and owner
        api_response = api_instance.update_project(project_id, project_update_req=project_update_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 
 **project_update_req** | [**ProjectUpdateReq**](ProjectUpdateReq.md)| Json object containing  **new_name**, **new_description** and/or **new_owner**. Note that only users subscribed to the project can be project owners. The project owner is the only one authorized to call this method. | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project successfully updated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

