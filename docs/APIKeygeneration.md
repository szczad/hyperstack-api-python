# APIKeygeneration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.api_keygeneration import APIKeygeneration

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeygeneration from a JSON string
api_keygeneration_instance = APIKeygeneration.from_json(json)
# print the JSON string representation of the object
print APIKeygeneration.to_json()

# convert the object into a dict
api_keygeneration_dict = api_keygeneration_instance.to_dict()
# create an instance of APIKeygeneration from a dict
api_keygeneration_form_dict = api_keygeneration.from_dict(api_keygeneration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


