# nexus-sdk.AdminApi

All URIs are relative to *https://scientia.atinary.com/nexus/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_information**](AdminApi.md#service_information) | **GET** /ServiceInfo | Service information.


# **service_information**
> ServiceInfoResponse service_information()

Service information.

Get service configuration information.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import nexus-sdk
from nexus-sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus-sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = nexus-sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus-sdk.AdminApi(api_client)
    
    try:
        # Service information.
        api_response = api_instance.service_information()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->service_information: %s\n" % e)
```

* Bearer (JWT) Authentication (tokens):
```python
from __future__ import print_function
import time
import nexus-sdk
from nexus-sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus-sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = nexus-sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Configure Bearer authorization (JWT): tokens
configuration = nexus-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with nexus-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nexus-sdk.AdminApi(api_client)
    
    try:
        # Service information.
        api_response = api_instance.service_information()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->service_information: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceInfoResponse**](ServiceInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [tokens](../README.md#tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

