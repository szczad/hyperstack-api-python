# UserTransferPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**role** | **str** |  | 

## Example

```python
from hyperstack.models.user_transfer_payload import UserTransferPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserTransferPayload from a JSON string
user_transfer_payload_instance = UserTransferPayload.from_json(json)
# print the JSON string representation of the object
print(UserTransferPayload.to_json())

# convert the object into a dict
user_transfer_payload_dict = user_transfer_payload_instance.to_dict()
# create an instance of UserTransferPayload from a dict
user_transfer_payload_form_dict = user_transfer_payload.from_dict(user_transfer_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


