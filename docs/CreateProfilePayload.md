# CreateProfilePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**data** | **Dict[str, str]** |  | 

## Example

```python
from hyperstack.models.create_profile_payload import CreateProfilePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfilePayload from a JSON string
create_profile_payload_instance = CreateProfilePayload.from_json(json)
# print the JSON string representation of the object
print CreateProfilePayload.to_json()

# convert the object into a dict
create_profile_payload_dict = create_profile_payload_instance.to_dict()
# create an instance of CreateProfilePayload from a dict
create_profile_payload_form_dict = create_profile_payload.from_dict(create_profile_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


