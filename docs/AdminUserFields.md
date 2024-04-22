# AdminUserFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**org_id** | **int** |  | 
**org_name** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**last_login** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_user_fields import AdminUserFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserFields from a JSON string
admin_user_fields_instance = AdminUserFields.from_json(json)
# print the JSON string representation of the object
print(AdminUserFields.to_json())

# convert the object into a dict
admin_user_fields_dict = admin_user_fields_instance.to_dict()
# create an instance of AdminUserFields from a dict
admin_user_fields_form_dict = admin_user_fields.from_dict(admin_user_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


