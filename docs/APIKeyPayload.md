# APIKeyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.api_key_payload import APIKeyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyPayload from a JSON string
api_key_payload_instance = APIKeyPayload.from_json(json)
# print the JSON string representation of the object
print APIKeyPayload.to_json()

# convert the object into a dict
api_key_payload_dict = api_key_payload_instance.to_dict()
# create an instance of APIKeyPayload from a dict
api_key_payload_form_dict = api_key_payload.from_dict(api_key_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


