# AdminOrganizationResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**environments** | [**List[AdminEnvrionmentResources]**](AdminEnvrionmentResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_organization_resources import AdminOrganizationResources

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationResources from a JSON string
admin_organization_resources_instance = AdminOrganizationResources.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationResources.to_json())

# convert the object into a dict
admin_organization_resources_dict = admin_organization_resources_instance.to_dict()
# create an instance of AdminOrganizationResources from a dict
admin_organization_resources_form_dict = admin_organization_resources.from_dict(admin_organization_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


