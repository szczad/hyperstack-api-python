# AdminFlavorResourcesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**flavors** | [**List[AdminFlavorResource]**](AdminFlavorResource.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_flavor_resources_list import AdminFlavorResourcesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFlavorResourcesList from a JSON string
admin_flavor_resources_list_instance = AdminFlavorResourcesList.from_json(json)
# print the JSON string representation of the object
print(AdminFlavorResourcesList.to_json())

# convert the object into a dict
admin_flavor_resources_list_dict = admin_flavor_resources_list_instance.to_dict()
# create an instance of AdminFlavorResourcesList from a dict
admin_flavor_resources_list_form_dict = admin_flavor_resources_list.from_dict(admin_flavor_resources_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


