# hyperstack.FloatingIpApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_public_ip_to_virtual_machine**](FloatingIpApi.md#attach_public_ip_to_virtual_machine) | **POST** /core/virtual-machines/{id}/attach-floatingip | Attach public IP to virtual machine
[**detach_public_ip_from_virtual_machine**](FloatingIpApi.md#detach_public_ip_from_virtual_machine) | **POST** /core/virtual-machines/{id}/detach-floatingip | Detach public IP from virtual machine


# **attach_public_ip_to_virtual_machine**
> ResponseModel attach_public_ip_to_virtual_machine(id)

Attach public IP to virtual machine

Initiates the creation of a public IP address and attaches it to an existing virtual machine, making it accessible through the internet. Include the virtual machine ID in the path to attach a public IP to the specified VM. For more information on public IP addresses, [**click here**](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/public-ip).

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
    api_instance = hyperstack.FloatingIpApi(api_client)
    id = 56 # int | 

    try:
        # Attach public IP to virtual machine
        api_response = api_instance.attach_public_ip_to_virtual_machine(id)
        print("The response of FloatingIpApi->attach_public_ip_to_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpApi->attach_public_ip_to_virtual_machine: %s\n" % e)
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
**200** | Public IP successfully attached to VM. |  -  |
**400** | Insufficient balance to create the resource |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_public_ip_from_virtual_machine**
> ResponseModel detach_public_ip_from_virtual_machine(id)

Detach public IP from virtual machine

Removes a public IP address from an existing virtual machine, disabling internet accessibility to the VM. Include the virtual machine ID in the path to detach the public IP from the specified VM. For more information on public IP addresses, [**click here**](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/public-ip).

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
    api_instance = hyperstack.FloatingIpApi(api_client)
    id = 56 # int | 

    try:
        # Detach public IP from virtual machine
        api_response = api_instance.detach_public_ip_from_virtual_machine(id)
        print("The response of FloatingIpApi->detach_public_ip_from_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIpApi->detach_public_ip_from_virtual_machine: %s\n" % e)
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

