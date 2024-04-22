# AdminHibernationRestorationPayloadModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**vm_name** | **str** |  | 
**vm_id** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from hyperstack.models.admin_hibernation_restoration_payload_model import AdminHibernationRestorationPayloadModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminHibernationRestorationPayloadModel from a JSON string
admin_hibernation_restoration_payload_model_instance = AdminHibernationRestorationPayloadModel.from_json(json)
# print the JSON string representation of the object
print(AdminHibernationRestorationPayloadModel.to_json())

# convert the object into a dict
admin_hibernation_restoration_payload_model_dict = admin_hibernation_restoration_payload_model_instance.to_dict()
# create an instance of AdminHibernationRestorationPayloadModel from a dict
admin_hibernation_restoration_payload_model_form_dict = admin_hibernation_restoration_payload_model.from_dict(admin_hibernation_restoration_payload_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


