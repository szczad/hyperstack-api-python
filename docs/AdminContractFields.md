# AdminContractFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**org_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**gpu_name** | **str** |  | [optional] 
**percent** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**resource_count** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_contract_fields import AdminContractFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminContractFields from a JSON string
admin_contract_fields_instance = AdminContractFields.from_json(json)
# print the JSON string representation of the object
print(AdminContractFields.to_json())

# convert the object into a dict
admin_contract_fields_dict = admin_contract_fields_instance.to_dict()
# create an instance of AdminContractFields from a dict
admin_contract_fields_form_dict = admin_contract_fields.from_dict(admin_contract_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


