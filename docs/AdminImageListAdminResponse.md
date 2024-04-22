# AdminImageListAdminResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**List[AdminImageAdminFields]**](AdminImageAdminFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_image_list_admin_response import AdminImageListAdminResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImageListAdminResponse from a JSON string
admin_image_list_admin_response_instance = AdminImageListAdminResponse.from_json(json)
# print the JSON string representation of the object
print(AdminImageListAdminResponse.to_json())

# convert the object into a dict
admin_image_list_admin_response_dict = admin_image_list_admin_response_instance.to_dict()
# create an instance of AdminImageListAdminResponse from a dict
admin_image_list_admin_response_form_dict = admin_image_list_admin_response.from_dict(admin_image_list_admin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


