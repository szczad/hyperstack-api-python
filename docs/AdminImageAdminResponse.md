# AdminImageAdminResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**image** | [**AdminImageAdminResponseImage**](AdminImageAdminResponseImage.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_image_admin_response import AdminImageAdminResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImageAdminResponse from a JSON string
admin_image_admin_response_instance = AdminImageAdminResponse.from_json(json)
# print the JSON string representation of the object
print(AdminImageAdminResponse.to_json())

# convert the object into a dict
admin_image_admin_response_dict = admin_image_admin_response_instance.to_dict()
# create an instance of AdminImageAdminResponse from a dict
admin_image_admin_response_form_dict = admin_image_admin_response.from_dict(admin_image_admin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


