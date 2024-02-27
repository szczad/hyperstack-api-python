# Invites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**invites** | [**List[InviteFields]**](InviteFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.invites import Invites

# TODO update the JSON string below
json = "{}"
# create an instance of Invites from a JSON string
invites_instance = Invites.from_json(json)
# print the JSON string representation of the object
print Invites.to_json()

# convert the object into a dict
invites_dict = invites_instance.to_dict()
# create an instance of Invites from a dict
invites_form_dict = invites.from_dict(invites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


