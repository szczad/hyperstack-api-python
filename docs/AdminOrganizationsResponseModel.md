# AdminOrganizationsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**List[OrganizationFields]**](OrganizationFields.md) |  | [optional] 
**organization_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.admin_organizations_response_model import AdminOrganizationsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationsResponseModel from a JSON string
admin_organizations_response_model_instance = AdminOrganizationsResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationsResponseModel.to_json())

# convert the object into a dict
admin_organizations_response_model_dict = admin_organizations_response_model_instance.to_dict()
# create an instance of AdminOrganizationsResponseModel from a dict
admin_organizations_response_model_form_dict = admin_organizations_response_model.from_dict(admin_organizations_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


