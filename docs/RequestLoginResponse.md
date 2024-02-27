# RequestLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**RequestLoginDataResponse**](RequestLoginDataResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.request_login_response import RequestLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLoginResponse from a JSON string
request_login_response_instance = RequestLoginResponse.from_json(json)
# print the JSON string representation of the object
print RequestLoginResponse.to_json()

# convert the object into a dict
request_login_response_dict = request_login_response_instance.to_dict()
# create an instance of RequestLoginResponse from a dict
request_login_response_form_dict = request_login_response.from_dict(request_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


