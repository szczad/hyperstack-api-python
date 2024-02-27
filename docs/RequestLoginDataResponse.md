# RequestLoginDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.request_login_data_response import RequestLoginDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLoginDataResponse from a JSON string
request_login_data_response_instance = RequestLoginDataResponse.from_json(json)
# print the JSON string representation of the object
print RequestLoginDataResponse.to_json()

# convert the object into a dict
request_login_data_response_dict = request_login_data_response_instance.to_dict()
# create an instance of RequestLoginDataResponse from a dict
request_login_data_response_form_dict = request_login_data_response.from_dict(request_login_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


