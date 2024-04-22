# AdminVersionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.admin_version_response_model import AdminVersionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVersionResponseModel from a JSON string
admin_version_response_model_instance = AdminVersionResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminVersionResponseModel.to_json())

# convert the object into a dict
admin_version_response_model_dict = admin_version_response_model_instance.to_dict()
# create an instance of AdminVersionResponseModel from a dict
admin_version_response_model_form_dict = admin_version_response_model.from_dict(admin_version_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


