# RemoveMemberFromOrganizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.remove_member_from_organization_response_model import RemoveMemberFromOrganizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMemberFromOrganizationResponseModel from a JSON string
remove_member_from_organization_response_model_instance = RemoveMemberFromOrganizationResponseModel.from_json(json)
# print the JSON string representation of the object
print(RemoveMemberFromOrganizationResponseModel.to_json())

# convert the object into a dict
remove_member_from_organization_response_model_dict = remove_member_from_organization_response_model_instance.to_dict()
# create an instance of RemoveMemberFromOrganizationResponseModel from a dict
remove_member_from_organization_response_model_form_dict = remove_member_from_organization_response_model.from_dict(remove_member_from_organization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


