# Invite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**invite** | [**InviteFields**](InviteFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.invite import Invite

# TODO update the JSON string below
json = "{}"
# create an instance of Invite from a JSON string
invite_instance = Invite.from_json(json)
# print the JSON string representation of the object
print Invite.to_json()

# convert the object into a dict
invite_dict = invite_instance.to_dict()
# create an instance of Invite from a dict
invite_form_dict = invite.from_dict(invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


