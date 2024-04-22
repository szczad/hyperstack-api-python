# AdminOrganizationResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**List[AdminOrganizationResources]**](AdminOrganizationResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_organization_resource_list import AdminOrganizationResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationResourceList from a JSON string
admin_organization_resource_list_instance = AdminOrganizationResourceList.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationResourceList.to_json())

# convert the object into a dict
admin_organization_resource_list_dict = admin_organization_resource_list_instance.to_dict()
# create an instance of AdminOrganizationResourceList from a dict
admin_organization_resource_list_form_dict = admin_organization_resource_list.from_dict(admin_organization_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


