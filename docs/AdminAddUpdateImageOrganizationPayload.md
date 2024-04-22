# AdminAddUpdateImageOrganizationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**openstack_id** | **str** |  | 
**region_id** | **int** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**size** | **int** |  | 
**is_public** | **bool** |  | 
**description** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**organizations** | **List[int]** |  | 

## Example

```python
from hyperstack.models.admin_add_update_image_organization_payload import AdminAddUpdateImageOrganizationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AdminAddUpdateImageOrganizationPayload from a JSON string
admin_add_update_image_organization_payload_instance = AdminAddUpdateImageOrganizationPayload.from_json(json)
# print the JSON string representation of the object
print(AdminAddUpdateImageOrganizationPayload.to_json())

# convert the object into a dict
admin_add_update_image_organization_payload_dict = admin_add_update_image_organization_payload_instance.to_dict()
# create an instance of AdminAddUpdateImageOrganizationPayload from a dict
admin_add_update_image_organization_payload_form_dict = admin_add_update_image_organization_payload.from_dict(admin_add_update_image_organization_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


