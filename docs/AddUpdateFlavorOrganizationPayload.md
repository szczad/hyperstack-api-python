# AddUpdateFlavorOrganizationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**openstack_id** | **str** |  | 
**region_id** | **int** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 
**disk** | **int** |  | 
**ephemeral** | **int** |  | [optional] 
**gpu_id** | **int** |  | 
**gpu_count** | **int** |  | 
**is_public** | **bool** |  | 
**organizations** | **List[int]** |  | 

## Example

```python
from hyperstack.models.add_update_flavor_organization_payload import AddUpdateFlavorOrganizationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AddUpdateFlavorOrganizationPayload from a JSON string
add_update_flavor_organization_payload_instance = AddUpdateFlavorOrganizationPayload.from_json(json)
# print the JSON string representation of the object
print(AddUpdateFlavorOrganizationPayload.to_json())

# convert the object into a dict
add_update_flavor_organization_payload_dict = add_update_flavor_organization_payload_instance.to_dict()
# create an instance of AddUpdateFlavorOrganizationPayload from a dict
add_update_flavor_organization_payload_form_dict = add_update_flavor_organization_payload.from_dict(add_update_flavor_organization_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


