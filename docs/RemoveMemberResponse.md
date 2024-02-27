# RemoveMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.remove_member_response import RemoveMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMemberResponse from a JSON string
remove_member_response_instance = RemoveMemberResponse.from_json(json)
# print the JSON string representation of the object
print RemoveMemberResponse.to_json()

# convert the object into a dict
remove_member_response_dict = remove_member_response_instance.to_dict()
# create an instance of RemoveMemberResponse from a dict
remove_member_response_form_dict = remove_member_response.from_dict(remove_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


