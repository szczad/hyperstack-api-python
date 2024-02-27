# hyperstack.TemplateApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /core/marketplace/templates | Create Template
[**delete_a_template**](TemplateApi.md#delete_a_template) | **DELETE** /core/marketplace/templates/{id} | Delete a Template
[**details_of_a_template_by_id**](TemplateApi.md#details_of_a_template_by_id) | **GET** /core/marketplace/templates/{id} | Details of a Template by ID
[**list_templates**](TemplateApi.md#list_templates) | **GET** /core/marketplace/templates | List Templates
[**update_template**](TemplateApi.md#update_template) | **PUT** /core/marketplace/templates/{id} | Update Template


# **create_template**
> Template create_template(name, description, is_public, content)

Create Template

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.template import Template
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
    api_instance = hyperstack.TemplateApi(api_client)
    name = 'name_example' # str | name is required
    description = 'description_example' # str | description is required
    is_public = 'is_public_example' # str | is_public is required
    content = None # bytearray | YAML file is required

    try:
        # Create Template
        api_response = api_instance.create_template(name, description, is_public, content)
        print("The response of TemplateApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name is required | 
 **description** | **str**| description is required | 
 **is_public** | **str**| is_public is required | 
 **content** | **bytearray**| YAML file is required | 

### Return type

[**Template**](Template.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template added successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_template**
> ResponseModel delete_a_template(id)

Delete a Template

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
    api_instance = hyperstack.TemplateApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Template
        api_response = api_instance.delete_a_template(id)
        print("The response of TemplateApi->delete_a_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_a_template: %s\n" % e)
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

# **details_of_a_template_by_id**
> Template details_of_a_template_by_id(id)

Details of a Template by ID

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.template import Template
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
    api_instance = hyperstack.TemplateApi(api_client)
    id = 56 # int | 

    try:
        # Details of a Template by ID
        api_response = api_instance.details_of_a_template_by_id(id)
        print("The response of TemplateApi->details_of_a_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->details_of_a_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Template**](Template.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting template detail success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> Templates list_templates(visibility=visibility)

List Templates

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.templates import Templates
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
    api_instance = hyperstack.TemplateApi(api_client)
    visibility = None # object | visibility: public/private (optional)

    try:
        # List Templates
        api_response = api_instance.list_templates(visibility=visibility)
        print("The response of TemplateApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | [**object**](.md)| visibility: public/private | [optional] 

### Return type

[**Templates**](Templates.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting templates success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**406** | Not Acceptable |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> Template update_template(id, payload)

Update Template

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.template import Template
from hyperstack.models.update_template import UpdateTemplate
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
    api_instance = hyperstack.TemplateApi(api_client)
    id = 56 # int | 
    payload = hyperstack.UpdateTemplate() # UpdateTemplate | 

    try:
        # Update Template
        api_response = api_instance.update_template(id, payload)
        print("The response of TemplateApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**UpdateTemplate**](UpdateTemplate.md)|  | 

### Return type

[**Template**](Template.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

