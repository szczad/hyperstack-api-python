# ProfileListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**profiles** | [**List[ProfileFields]**](ProfileFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.profile_list_response import ProfileListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileListResponse from a JSON string
profile_list_response_instance = ProfileListResponse.from_json(json)
# print the JSON string representation of the object
print ProfileListResponse.to_json()

# convert the object into a dict
profile_list_response_dict = profile_list_response_instance.to_dict()
# create an instance of ProfileListResponse from a dict
profile_list_response_form_dict = profile_list_response.from_dict(profile_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


