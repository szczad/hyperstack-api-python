# hyperstack.VolumeAttachmentApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_volumes_to_virtual_machine**](VolumeAttachmentApi.md#attach_volumes_to_virtual_machine) | **POST** /core/virtual-machines/{virtual_machine_id}/attach-volumes | Attach volumes to virtual machine
[**detach_volumes_from_virtual_machine**](VolumeAttachmentApi.md#detach_volumes_from_virtual_machine) | **POST** /core/virtual-machines/{virtual_machine_id}/detach-volumes | Detach volumes from virtual machine


# **attach_volumes_to_virtual_machine**
> AttachVolumes attach_volumes_to_virtual_machine(virtual_machine_id, payload)

Attach volumes to virtual machine

Attaches one or more volumes to an existing virtual machine, expanding its storage capacity by 2PB per attached volume. Include the virtual machine ID in the path and the volume IDs in the request body to attach the specified volumes to the designated virtual machine. For additional details on volume attachment, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/volumes-available-features#attach-a-volume-to-a-virtual-machine-1).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.attach_volumes import AttachVolumes
from hyperstack.models.attach_volumes_payload import AttachVolumesPayload
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
    api_instance = hyperstack.VolumeAttachmentApi(api_client)
    virtual_machine_id = 56 # int | 
    payload = hyperstack.AttachVolumesPayload() # AttachVolumesPayload | 

    try:
        # Attach volumes to virtual machine
        api_response = api_instance.attach_volumes_to_virtual_machine(virtual_machine_id, payload)
        print("The response of VolumeAttachmentApi->attach_volumes_to_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeAttachmentApi->attach_volumes_to_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **payload** | [**AttachVolumesPayload**](AttachVolumesPayload.md)|  | 

### Return type

[**AttachVolumes**](AttachVolumes.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volumes have been successfully attached to the virtual machine. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_volumes_from_virtual_machine**
> DetachVolumes detach_volumes_from_virtual_machine(virtual_machine_id, payload)

Detach volumes from virtual machine

Detaches one or more volumes currently attached to an existing virtual machine. Include the virtual machine ID in the path and the volume IDs in the request body to detach the specified volumes from the designated virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.detach_volumes import DetachVolumes
from hyperstack.models.detach_volumes_payload import DetachVolumesPayload
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
    api_instance = hyperstack.VolumeAttachmentApi(api_client)
    virtual_machine_id = 56 # int | 
    payload = hyperstack.DetachVolumesPayload() # DetachVolumesPayload | 

    try:
        # Detach volumes from virtual machine
        api_response = api_instance.detach_volumes_from_virtual_machine(virtual_machine_id, payload)
        print("The response of VolumeAttachmentApi->detach_volumes_from_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeAttachmentApi->detach_volumes_from_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **payload** | [**DetachVolumesPayload**](DetachVolumesPayload.md)|  | 

### Return type

[**DetachVolumes**](DetachVolumes.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volumes have been successfully detached from the virtual machine. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

