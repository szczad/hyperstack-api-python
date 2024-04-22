# hyperstack.CallbacksApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_callback_to_virtual_machine**](CallbacksApi.md#attach_callback_to_virtual_machine) | **POST** /core/virtual-machines/{id}/attach-callback | Attach callback to virtual machine
[**attach_callback_to_volume**](CallbacksApi.md#attach_callback_to_volume) | **POST** /core/volumes/{id}/attach-callback | Attach callback to volume
[**delete_virtual_machine_callback**](CallbacksApi.md#delete_virtual_machine_callback) | **DELETE** /core/virtual-machines/{id}/delete-callback | Delete virtual machine callback
[**delete_volume_callback**](CallbacksApi.md#delete_volume_callback) | **DELETE** /core/volumes/{id}/delete-callback | Delete volume callback
[**update_virtual_machine_callback**](CallbacksApi.md#update_virtual_machine_callback) | **PUT** /core/virtual-machines/{id}/update-callback | Update virtual machine callback
[**update_volume_callback**](CallbacksApi.md#update_volume_callback) | **PUT** /core/volumes/{id}/update-callback | Update volume callback


# **attach_callback_to_virtual_machine**
> AttachCallbackResponse attach_callback_to_virtual_machine(id, payload)

Attach callback to virtual machine

Creates a callback URL for a specified virtual machine, enabling the posting of action events executed on the virtual machine to the specified URL. Provide the callback URL in the request body and the ID of the virtual machine to which it is being attached in the path. For more details on virtual machine callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks#attach-a-callback-url-to-an-existing-virtual-machine).

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
        # Attach callback to virtual machine
        api_response = api_instance.attach_callback_to_virtual_machine(id, payload)
        print("The response of CallbacksApi->attach_callback_to_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->attach_callback_to_virtual_machine: %s\n" % e)
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
**200** | Callback URL successfully attached to your virtual machine. Any action events on your virtual machine will be posted to the provided URL |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_callback_to_volume**
> AttachCallbackResponse attach_callback_to_volume(id, payload)

Attach callback to volume

Creates a callback URL for a specified volume, enabling the posting of action events executed on the volume to the specified URL. Provide the callback URL in the request body and the ID of the volume to which it is being attached in the path. For more details on volume callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks).

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
        # Attach callback to volume
        api_response = api_instance.attach_callback_to_volume(id, payload)
        print("The response of CallbacksApi->attach_callback_to_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->attach_callback_to_volume: %s\n" % e)
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

# **delete_virtual_machine_callback**
> ResponseModel delete_virtual_machine_callback(id)

Delete virtual machine callback

Permanently deletes the callback URL associated with a specified virtual machine by providing the virtual machine ID in the request path. For additional information on virtual machine callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks).

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
        # Delete virtual machine callback
        api_response = api_instance.delete_virtual_machine_callback(id)
        print("The response of CallbacksApi->delete_virtual_machine_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->delete_virtual_machine_callback: %s\n" % e)
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
**200** | Virtual machine callback URL successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume_callback**
> ResponseModel delete_volume_callback(id)

Delete volume callback

Permanently deletes the callback URL associated with a specified volume by providing the volume ID in the request path. For additional information on volume callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks).

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
        # Delete volume callback
        api_response = api_instance.delete_volume_callback(id)
        print("The response of CallbacksApi->delete_volume_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->delete_volume_callback: %s\n" % e)
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
**200** | Volume callback URL successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_machine_callback**
> AttachCallbackResponse update_virtual_machine_callback(id, payload)

Update virtual machine callback

Updates the callback URL for a specified virtual machine. Provide the new callback URL in the request body, along with the ID of the associated virtual machine in the path. For additional information on virtual machine callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks).

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
        # Update virtual machine callback
        api_response = api_instance.update_virtual_machine_callback(id, payload)
        print("The response of CallbacksApi->update_virtual_machine_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->update_virtual_machine_callback: %s\n" % e)
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
**200** | Virtual machine callback URL successfully updated. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_volume_callback**
> AttachCallbackResponse update_volume_callback(id, payload)

Update volume callback

Updates the callback URL for a specified volume. Provide the new callback URL in the request body, along with the ID of the associated volume in the path. For additional information on volume callback URLs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks).

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
        # Update volume callback
        api_response = api_instance.update_volume_callback(id, payload)
        print("The response of CallbacksApi->update_volume_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbacksApi->update_volume_callback: %s\n" % e)
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

