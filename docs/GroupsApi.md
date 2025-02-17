# nexus_sdk.GroupsApi

All URIs are relative to *https://api.enterprise.atinary.com/nexus/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /Groups/{group_id} | Delete all projects in a group


# **delete_group**
> GenericResponse delete_group(group_id)

Delete all projects in a group

Delete a Group. The group deletion causes the deletion of all projects, files, and subscriptions associated with it. Note that a group can only be deleted by an admin.

### Example

* Api Key Authentication (api_key):
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
    api_instance = nexus_sdk.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers

    try:
        # Delete all projects in a group
        api_response = api_instance.delete_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
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
    api_instance = nexus_sdk.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Group identifiers

    try:
        # Delete all projects in a group
        api_response = api_instance.delete_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group identifiers | 

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
**200** | Group successfully deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

