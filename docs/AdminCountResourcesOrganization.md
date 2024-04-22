# AdminCountResourcesOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**total_instances** | **int** |  | [optional] 
**total_volumes** | **int** |  | [optional] 
**total_containers** | **int** |  | [optional] 
**total_clusters** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.admin_count_resources_organization import AdminCountResourcesOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCountResourcesOrganization from a JSON string
admin_count_resources_organization_instance = AdminCountResourcesOrganization.from_json(json)
# print the JSON string representation of the object
print(AdminCountResourcesOrganization.to_json())

# convert the object into a dict
admin_count_resources_organization_dict = admin_count_resources_organization_instance.to_dict()
# create an instance of AdminCountResourcesOrganization from a dict
admin_count_resources_organization_form_dict = admin_count_resources_organization.from_dict(admin_count_resources_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


