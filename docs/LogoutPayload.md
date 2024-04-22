# LogoutPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | 

## Example

```python
from hyperstack.models.logout_payload import LogoutPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutPayload from a JSON string
logout_payload_instance = LogoutPayload.from_json(json)
# print the JSON string representation of the object
print(LogoutPayload.to_json())

# convert the object into a dict
logout_payload_dict = logout_payload_instance.to_dict()
# create an instance of LogoutPayload from a dict
logout_payload_form_dict = logout_payload.from_dict(logout_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


