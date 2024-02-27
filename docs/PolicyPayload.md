# PolicyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**is_public** | **bool** |  | 
**permissions** | **List[int]** |  | 

## Example

```python
from hyperstack.models.policy_payload import PolicyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPayload from a JSON string
policy_payload_instance = PolicyPayload.from_json(json)
# print the JSON string representation of the object
print PolicyPayload.to_json()

# convert the object into a dict
policy_payload_dict = policy_payload_instance.to_dict()
# create an instance of PolicyPayload from a dict
policy_payload_form_dict = policy_payload.from_dict(policy_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


