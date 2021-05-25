# nexus_sdk.FilesApi

All URIs are relative to *https://scientia.atinary.com/nexus/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /Files/{file_id} | Delete a file
[**download_file**](FilesApi.md#download_file) | **GET** /Files/{file_id} | Download a file
[**list_files**](FilesApi.md#list_files) | **GET** /Files | List available files for a project
[**upload_file**](FilesApi.md#upload_file) | **POST** /Files | Upload a file under a project


# **delete_file**
> GenericResponse delete_file(file_id)

Delete a file

Delete a specific file.  Note that every file belongs to a project and only users subscribed to that project are authorized to request deletions on it.

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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | ID assigned to the file once it is uploaded.

    try:
        # Delete a file
        api_response = api_instance.delete_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | ID assigned to the file once it is uploaded.

    try:
        # Delete a file
        api_response = api_instance.delete_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ID assigned to the file once it is uploaded. | 

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
**200** | File successfully deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(file_id)

Download a file

Download a specific file. Note that every file belongs to a project and only users subscribed to the project are authorized to request downloads from it.

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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | ID assigned to the file once it is uploaded.

    try:
        # Download a file
        api_response = api_instance.download_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->download_file: %s\n" % e)
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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    file_id = 'file_id_example' # str | ID assigned to the file once it is uploaded.

    try:
        # Download a file
        api_response = api_instance.download_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ID assigned to the file once it is uploaded. | 

### Return type

**file**

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File successfully retrieved |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> ListFilesResponse list_files(project_id=project_id, group_type=group_type)

List available files for a project

List available files for a specific project. Note that only users subscribed to the project can list its files.

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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    project_id = 'project_id_example' # str | **Required** ID assigned to the project once created in Atinary™ Nexus. (optional)
group_type = 'group_type_example' # str | String indicating how the file is classified. Available values are *parameters*, *properties* or *other*. (optional)

    try:
        # List available files for a project
        api_response = api_instance.list_files(project_id=project_id, group_type=group_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    project_id = 'project_id_example' # str | **Required** ID assigned to the project once created in Atinary™ Nexus. (optional)
group_type = 'group_type_example' # str | String indicating how the file is classified. Available values are *parameters*, *properties* or *other*. (optional)

    try:
        # List available files for a project
        api_response = api_instance.list_files(project_id=project_id, group_type=group_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| **Required** ID assigned to the project once created in Atinary™ Nexus. | [optional] 
 **group_type** | **str**| String indicating how the file is classified. Available values are *parameters*, *properties* or *other*. | [optional] 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

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
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> UploadResponse upload_file(project_id, group_type, inline_object=inline_object)

Upload a file under a project

Upload a file under a specific project. Note that only users subscribed to the project can upload files to it. 

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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
group_type = 'group_type_example' # str | String indicating how the file is classified. Available values are *parameters*, *properties* or *other*.
inline_object = nexus_sdk.InlineObject() # InlineObject |  (optional)

    try:
        # Upload a file under a project
        api_response = api_instance.upload_file(project_id, group_type, inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
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
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api/latest",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus_sdk.FilesApi(api_client)
    project_id = 'project_id_example' # str | ID assigned to the project once created in Atinary™ Nexus.
group_type = 'group_type_example' # str | String indicating how the file is classified. Available values are *parameters*, *properties* or *other*.
inline_object = nexus_sdk.InlineObject() # InlineObject |  (optional)

    try:
        # Upload a file under a project
        api_response = api_instance.upload_file(project_id, group_type, inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID assigned to the project once created in Atinary™ Nexus. | 
 **group_type** | **str**| String indicating how the file is classified. Available values are *parameters*, *properties* or *other*. | 
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File successfully uploaded |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

