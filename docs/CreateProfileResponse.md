# CreateProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**profile** | [**ProfileFields**](ProfileFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.create_profile_response import CreateProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileResponse from a JSON string
create_profile_response_instance = CreateProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CreateProfileResponse.to_json())

# convert the object into a dict
create_profile_response_dict = create_profile_response_instance.to_dict()
# create an instance of CreateProfileResponse from a dict
create_profile_response_form_dict = create_profile_response.from_dict(create_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


