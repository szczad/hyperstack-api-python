# OrganizationResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**environments** | [**List[EnvrionmentResources]**](EnvrionmentResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_resources import OrganizationResources

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResources from a JSON string
organization_resources_instance = OrganizationResources.from_json(json)
# print the JSON string representation of the object
print OrganizationResources.to_json()

# convert the object into a dict
organization_resources_dict = organization_resources_instance.to_dict()
# create an instance of OrganizationResources from a dict
organization_resources_form_dict = organization_resources.from_dict(organization_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


