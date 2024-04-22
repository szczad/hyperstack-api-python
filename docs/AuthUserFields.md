# AuthUserFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.auth_user_fields import AuthUserFields

# TODO update the JSON string below
json = "{}"
# create an instance of AuthUserFields from a JSON string
auth_user_fields_instance = AuthUserFields.from_json(json)
# print the JSON string representation of the object
print(AuthUserFields.to_json())

# convert the object into a dict
auth_user_fields_dict = auth_user_fields_instance.to_dict()
# create an instance of AuthUserFields from a dict
auth_user_fields_form_dict = auth_user_fields.from_dict(auth_user_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


