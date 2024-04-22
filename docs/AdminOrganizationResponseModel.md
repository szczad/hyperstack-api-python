# AdminOrganizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**OrganizationFields**](OrganizationFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_organization_response_model import AdminOrganizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationResponseModel from a JSON string
admin_organization_response_model_instance = AdminOrganizationResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationResponseModel.to_json())

# convert the object into a dict
admin_organization_response_model_dict = admin_organization_response_model_instance.to_dict()
# create an instance of AdminOrganizationResponseModel from a dict
admin_organization_response_model_form_dict = admin_organization_response_model.from_dict(admin_organization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


