# OrganizationFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**credit** | **int** |  | [optional] 
**threshold** | **int** |  | [optional] 
**total_instances** | **int** |  | [optional] 
**total_volumes** | **int** |  | [optional] 
**total_containers** | **int** |  | [optional] 
**total_clusters** | **int** |  | [optional] 
**users** | [**List[OrganizationUserResponseModel]**](OrganizationUserResponseModel.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.organization_fields import OrganizationFields

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationFields from a JSON string
organization_fields_instance = OrganizationFields.from_json(json)
# print the JSON string representation of the object
print(OrganizationFields.to_json())

# convert the object into a dict
organization_fields_dict = organization_fields_instance.to_dict()
# create an instance of OrganizationFields from a dict
organization_fields_form_dict = organization_fields.from_dict(organization_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


