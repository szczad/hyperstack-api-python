# AttachCallbackPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from hyperstack.models.attach_callback_payload import AttachCallbackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachCallbackPayload from a JSON string
attach_callback_payload_instance = AttachCallbackPayload.from_json(json)
# print the JSON string representation of the object
print(AttachCallbackPayload.to_json())

# convert the object into a dict
attach_callback_payload_dict = attach_callback_payload_instance.to_dict()
# create an instance of AttachCallbackPayload from a dict
attach_callback_payload_form_dict = attach_callback_payload.from_dict(attach_callback_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


