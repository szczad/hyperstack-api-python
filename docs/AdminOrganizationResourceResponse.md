# AdminOrganizationResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organization** | [**AdminOrganizationResources**](AdminOrganizationResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_organization_resource_response import AdminOrganizationResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationResourceResponse from a JSON string
admin_organization_resource_response_instance = AdminOrganizationResourceResponse.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationResourceResponse.to_json())

# convert the object into a dict
admin_organization_resource_response_dict = admin_organization_resource_response_instance.to_dict()
# create an instance of AdminOrganizationResourceResponse from a dict
admin_organization_resource_response_form_dict = admin_organization_resource_response.from_dict(admin_organization_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


