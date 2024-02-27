# hyperstack.ComplianceApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compliance**](ComplianceApi.md#create_compliance) | **POST** /core/compliance | Create Compliance
[**delete_a_compliance**](ComplianceApi.md#delete_a_compliance) | **DELETE** /core/compliance/{gpu_model} | Delete a compliance
[**get_compliance_list**](ComplianceApi.md#get_compliance_list) | **GET** /core/compliance | Get Compliance List
[**update_a_compliance**](ComplianceApi.md#update_a_compliance) | **PUT** /core/compliance | Update a compliance


# **create_compliance**
> CreateUpdateComplianceResponse create_compliance(payload)

Create Compliance

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.compliance_payload import CompliancePayload
from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse
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
    api_instance = hyperstack.ComplianceApi(api_client)
    payload = hyperstack.CompliancePayload() # CompliancePayload | 

    try:
        # Create Compliance
        api_response = api_instance.create_compliance(payload)
        print("The response of ComplianceApi->create_compliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->create_compliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CompliancePayload**](CompliancePayload.md)|  | 

### Return type

[**CreateUpdateComplianceResponse**](CreateUpdateComplianceResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_compliance**
> ResponseModel delete_a_compliance(gpu_model)

Delete a compliance

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
    api_instance = hyperstack.ComplianceApi(api_client)
    gpu_model = 'gpu_model_example' # str | 

    try:
        # Delete a compliance
        api_response = api_instance.delete_a_compliance(gpu_model)
        print("The response of ComplianceApi->delete_a_compliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->delete_a_compliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu_model** | **str**|  | 

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

# **get_compliance_list**
> ComplianceResponse get_compliance_list(gpu=gpu)

Get Compliance List

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.compliance_response import ComplianceResponse
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
    api_instance = hyperstack.ComplianceApi(api_client)
    gpu = None # object | This is for gpu model (optional)

    try:
        # Get Compliance List
        api_response = api_instance.get_compliance_list(gpu=gpu)
        print("The response of ComplianceApi->get_compliance_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu** | [**object**](.md)| This is for gpu model | [optional] 

### Return type

[**ComplianceResponse**](ComplianceResponse.md)

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
**406** | Not Acceptable |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_compliance**
> CreateUpdateComplianceResponse update_a_compliance(payload)

Update a compliance

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.compliance_payload import CompliancePayload
from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse
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
    api_instance = hyperstack.ComplianceApi(api_client)
    payload = hyperstack.CompliancePayload() # CompliancePayload | 

    try:
        # Update a compliance
        api_response = api_instance.update_a_compliance(payload)
        print("The response of ComplianceApi->update_a_compliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_a_compliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CompliancePayload**](CompliancePayload.md)|  | 

### Return type

[**CreateUpdateComplianceResponse**](CreateUpdateComplianceResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

