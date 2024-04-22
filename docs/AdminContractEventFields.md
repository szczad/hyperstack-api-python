# AdminContractEventFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_contract_event_fields import AdminContractEventFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractEventFields from a JSON string
admin_contract_event_fields_instance = AdminContractEventFields.from_json(json)
# print the JSON string representation of the object
print(AdminContractEventFields.to_json())

# convert the object into a dict
admin_contract_event_fields_dict = admin_contract_event_fields_instance.to_dict()
# create an instance of AdminContractEventFields from a dict
admin_contract_event_fields_form_dict = admin_contract_event_fields.from_dict(admin_contract_event_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


