# CreateUpdatePermissionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**permission** | [**PermissionFields**](PermissionFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.create_update_permission_response_model import CreateUpdatePermissionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdatePermissionResponseModel from a JSON string
create_update_permission_response_model_instance = CreateUpdatePermissionResponseModel.from_json(json)
# print the JSON string representation of the object
print(CreateUpdatePermissionResponseModel.to_json())

# convert the object into a dict
create_update_permission_response_model_dict = create_update_permission_response_model_instance.to_dict()
# create an instance of CreateUpdatePermissionResponseModel from a dict
create_update_permission_response_model_form_dict = create_update_permission_response_model.from_dict(create_update_permission_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


