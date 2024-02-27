# UserInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**user** | [**UserFields**](UserFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.user_info_response import UserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoResponse from a JSON string
user_info_response_instance = UserInfoResponse.from_json(json)
# print the JSON string representation of the object
print UserInfoResponse.to_json()

# convert the object into a dict
user_info_response_dict = user_info_response_instance.to_dict()
# create an instance of UserInfoResponse from a dict
user_info_response_form_dict = user_info_response.from_dict(user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


