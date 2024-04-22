# UsersInfoListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**users_info** | [**UsersInfoFields**](UsersInfoFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.users_info_list_response import UsersInfoListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfoListResponse from a JSON string
users_info_list_response_instance = UsersInfoListResponse.from_json(json)
# print the JSON string representation of the object
print(UsersInfoListResponse.to_json())

# convert the object into a dict
users_info_list_response_dict = users_info_list_response_instance.to_dict()
# create an instance of UsersInfoListResponse from a dict
users_info_list_response_form_dict = users_info_list_response.from_dict(users_info_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


