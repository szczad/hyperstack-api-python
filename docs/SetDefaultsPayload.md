# SetDefaultsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavors** | **List[int]** |  | 
**images** | **List[int]** |  | 

## Example

```python
from hyperstack.models.set_defaults_payload import SetDefaultsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultsPayload from a JSON string
set_defaults_payload_instance = SetDefaultsPayload.from_json(json)
# print the JSON string representation of the object
print(SetDefaultsPayload.to_json())

# convert the object into a dict
set_defaults_payload_dict = set_defaults_payload_instance.to_dict()
# create an instance of SetDefaultsPayload from a dict
set_defaults_payload_form_dict = set_defaults_payload.from_dict(set_defaults_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


