# GetInvitesResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**invites** | [**List[InviteFields]**](InviteFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_invites_response_model import GetInvitesResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvitesResponseModel from a JSON string
get_invites_response_model_instance = GetInvitesResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetInvitesResponseModel.to_json())

# convert the object into a dict
get_invites_response_model_dict = get_invites_response_model_instance.to_dict()
# create an instance of GetInvitesResponseModel from a dict
get_invites_response_model_form_dict = get_invites_response_model.from_dict(get_invites_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


