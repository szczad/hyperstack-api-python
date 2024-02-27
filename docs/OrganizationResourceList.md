# OrganizationResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**List[OrganizationResources]**](OrganizationResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_resource_list import OrganizationResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResourceList from a JSON string
organization_resource_list_instance = OrganizationResourceList.from_json(json)
# print the JSON string representation of the object
print OrganizationResourceList.to_json()

# convert the object into a dict
organization_resource_list_dict = organization_resource_list_instance.to_dict()
# create an instance of OrganizationResourceList from a dict
organization_resource_list_form_dict = organization_resource_list.from_dict(organization_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


