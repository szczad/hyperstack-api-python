# AdminGetContractDetailFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_get_contract_detail_fields import AdminGetContractDetailFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGetContractDetailFields from a JSON string
admin_get_contract_detail_fields_instance = AdminGetContractDetailFields.from_json(json)
# print the JSON string representation of the object
print(AdminGetContractDetailFields.to_json())

# convert the object into a dict
admin_get_contract_detail_fields_dict = admin_get_contract_detail_fields_instance.to_dict()
# create an instance of AdminGetContractDetailFields from a dict
admin_get_contract_detail_fields_form_dict = admin_get_contract_detail_fields.from_dict(admin_get_contract_detail_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


