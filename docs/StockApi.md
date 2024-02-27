# hyperstack.StockApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_stocks**](StockApi.md#retrieve_stocks) | **GET** /core/stocks | 


# **retrieve_stocks**
> NewStockRetriveResponse retrieve_stocks()



### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.new_stock_retrive_response import NewStockRetriveResponse
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
    api_instance = hyperstack.StockApi(api_client)

    try:
        api_response = api_instance.retrieve_stocks()
        print("The response of StockApi->retrieve_stocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->retrieve_stocks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewStockRetriveResponse**](NewStockRetriveResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stocks Retrived Successfully. |  -  |
**401** | Unauthorized |  -  |
**404** | Stocks Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

