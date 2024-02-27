# hyperstack.VirtualMachineEventsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_of_the_instance_events**](VirtualMachineEventsApi.md#fetch_all_of_the_instance_events) | **GET** /core/virtual-machines/{virtual_machine_id}/events | Fetch all of the instance events


# **fetch_all_of_the_instance_events**
> InstanceEvents fetch_all_of_the_instance_events(virtual_machine_id)

Fetch all of the instance events

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.instance_events import InstanceEvents
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
    api_instance = hyperstack.VirtualMachineEventsApi(api_client)
    virtual_machine_id = 'virtual_machine_id_example' # str | 

    try:
        # Fetch all of the instance events
        api_response = api_instance.fetch_all_of_the_instance_events(virtual_machine_id)
        print("The response of VirtualMachineEventsApi->fetch_all_of_the_instance_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineEventsApi->fetch_all_of_the_instance_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **str**|  | 

### Return type

[**InstanceEvents**](InstanceEvents.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting instance events success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

