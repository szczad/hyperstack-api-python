# RemoveMemberPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from hyperstack.models.remove_member_payload import RemoveMemberPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMemberPayload from a JSON string
remove_member_payload_instance = RemoveMemberPayload.from_json(json)
# print the JSON string representation of the object
print(RemoveMemberPayload.to_json())

# convert the object into a dict
remove_member_payload_dict = remove_member_payload_instance.to_dict()
# create an instance of RemoveMemberPayload from a dict
remove_member_payload_form_dict = remove_member_payload.from_dict(remove_member_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


