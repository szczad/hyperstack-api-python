# InviteUserPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from hyperstack.models.invite_user_payload import InviteUserPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserPayload from a JSON string
invite_user_payload_instance = InviteUserPayload.from_json(json)
# print the JSON string representation of the object
print(InviteUserPayload.to_json())

# convert the object into a dict
invite_user_payload_dict = invite_user_payload_instance.to_dict()
# create an instance of InviteUserPayload from a dict
invite_user_payload_form_dict = invite_user_payload.from_dict(invite_user_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


