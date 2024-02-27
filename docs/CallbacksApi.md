# hyperstack.CallbacksApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_a_callback_to_a_volume**](CallbacksApi.md#attach_a_callback_to_a_volume) | **POST** /core/volumes/{id}/attach-callback | Attach a callback to a volume
[**attach_a_callback_to_an_instance**](CallbacksApi.md#attach_a_callback_to_an_instance) | **POST** /core/virtual-machines/{id}/attach-callback | Attach a callback to an instance
[**delete_a_callback_url_for_an_instance**](CallbacksApi.md#delete_a_callback_url_for_an_instance) | **DELETE** /core/virtual-machines/{id}/delete-callback | Delete a callback URL for an instance
[**delete_callback_url_for_a_volume**](CallbacksApi.md#delete_callback_url_for_a_volume) | **DELETE** /core/volumes/{id}/delete-callback | Delete callback URL for a volume
[**update_a_callback_url**](CallbacksApi.md#update_a_callback_url) | **PUT** /core/virtual-machines/{id}/update-callback | Update a callback URL
[**update_callback_url_for_volume**](CallbacksApi.md#update_callback_url_for_volume) | **PUT** /core/volumes/{id}/update-callback | Update callback URL for volume


# **attach_a_callback_to_a_volume**
> AttachCallbackResponse attach_a_callback_to_a_volume(id, payload)

Attach a callback to a volume

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.attach_callback_payload import AttachCallbackPayload
from hyperstack.models.attach_callback_response import AttachCallbackResponse
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 
    payload = hyperstack.AttachCallbackPayload() # AttachCallbackPayload | 

    try:
        # Attach a callback to a volume
        api_response = api_instance.attach_a_callback_to_a_volume(id, payload)
        print("The response of CallbacksApi->attach_a_callback_to_a_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->attach_a_callback_to_a_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**AttachCallbackPayload**](AttachCallbackPayload.md)|  | 

### Return type

[**AttachCallbackResponse**](AttachCallbackResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback URL successfully attached to your volume. Any action events on your volume will be posted to the provided URL |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_a_callback_to_an_instance**
> AttachCallbackResponse attach_a_callback_to_an_instance(id, payload)

Attach a callback to an instance

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.attach_callback_payload import AttachCallbackPayload
from hyperstack.models.attach_callback_response import AttachCallbackResponse
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 
    payload = hyperstack.AttachCallbackPayload() # AttachCallbackPayload | 

    try:
        # Attach a callback to an instance
        api_response = api_instance.attach_a_callback_to_an_instance(id, payload)
        print("The response of CallbacksApi->attach_a_callback_to_an_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->attach_a_callback_to_an_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**AttachCallbackPayload**](AttachCallbackPayload.md)|  | 

### Return type

[**AttachCallbackResponse**](AttachCallbackResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback URL successfully attached to your instance. Any action events on your instance will be posted to the provided URL |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_callback_url_for_an_instance**
> ResponseModel delete_a_callback_url_for_an_instance(id)

Delete a callback URL for an instance

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.response_model import ResponseModel
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 

    try:
        # Delete a callback URL for an instance
        api_response = api_instance.delete_a_callback_url_for_an_instance(id)
        print("The response of CallbacksApi->delete_a_callback_url_for_an_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->delete_a_callback_url_for_an_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_callback_url_for_a_volume**
> ResponseModel delete_callback_url_for_a_volume(id)

Delete callback URL for a volume

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.response_model import ResponseModel
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 

    try:
        # Delete callback URL for a volume
        api_response = api_instance.delete_callback_url_for_a_volume(id)
        print("The response of CallbacksApi->delete_callback_url_for_a_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->delete_callback_url_for_a_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_callback_url**
> AttachCallbackResponse update_a_callback_url(id, payload)

Update a callback URL

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.attach_callback_payload import AttachCallbackPayload
from hyperstack.models.attach_callback_response import AttachCallbackResponse
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 
    payload = hyperstack.AttachCallbackPayload() # AttachCallbackPayload | 

    try:
        # Update a callback URL
        api_response = api_instance.update_a_callback_url(id, payload)
        print("The response of CallbacksApi->update_a_callback_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->update_a_callback_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**AttachCallbackPayload**](AttachCallbackPayload.md)|  | 

### Return type

[**AttachCallbackResponse**](AttachCallbackResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback URL successfully updated. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_url_for_volume**
> AttachCallbackResponse update_callback_url_for_volume(id, payload)

Update callback URL for volume

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.attach_callback_payload import AttachCallbackPayload
from hyperstack.models.attach_callback_response import AttachCallbackResponse
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.CallbacksApi(api_client)
    id = 56 # int | 
    payload = hyperstack.AttachCallbackPayload() # AttachCallbackPayload | 

    try:
        # Update callback URL for volume
        api_response = api_instance.update_callback_url_for_volume(id, payload)
        print("The response of CallbacksApi->update_callback_url_for_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->update_callback_url_for_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**AttachCallbackPayload**](AttachCallbackPayload.md)|  | 

### Return type

[**AttachCallbackResponse**](AttachCallbackResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback URL successfully updated. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

