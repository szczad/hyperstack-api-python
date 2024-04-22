# AdminImageAdminFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**region_id** | **int** |  | [optional] 
**region_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**labels** | [**List[LableResonse]**](LableResonse.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_image_admin_fields import AdminImageAdminFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImageAdminFields from a JSON string
admin_image_admin_fields_instance = AdminImageAdminFields.from_json(json)
# print the JSON string representation of the object
print(AdminImageAdminFields.to_json())

# convert the object into a dict
admin_image_admin_fields_dict = admin_image_admin_fields_instance.to_dict()
# create an instance of AdminImageAdminFields from a dict
admin_image_admin_fields_form_dict = admin_image_admin_fields.from_dict(admin_image_admin_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


