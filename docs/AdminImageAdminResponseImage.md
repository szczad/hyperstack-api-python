# AdminImageAdminResponseImage


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
**organizations** | **List[int]** |  | 

## Example

```python
from hyperstack.models.admin_image_admin_response_image import AdminImageAdminResponseImage

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImageAdminResponseImage from a JSON string
admin_image_admin_response_image_instance = AdminImageAdminResponseImage.from_json(json)
# print the JSON string representation of the object
print(AdminImageAdminResponseImage.to_json())

# convert the object into a dict
admin_image_admin_response_image_dict = admin_image_admin_response_image_instance.to_dict()
# create an instance of AdminImageAdminResponseImage from a dict
admin_image_admin_response_image_form_dict = admin_image_admin_response_image.from_dict(admin_image_admin_response_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


