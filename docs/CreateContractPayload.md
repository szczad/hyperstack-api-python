# CreateContractPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**description** | **str** |  | [optional] 
**discount_resources** | [**List[ResourcePayload]**](ResourcePayload.md) |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | 

## Example

```python
from hyperstack.models.create_contract_payload import CreateContractPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractPayload from a JSON string
create_contract_payload_instance = CreateContractPayload.from_json(json)
# print the JSON string representation of the object
print(CreateContractPayload.to_json())

# convert the object into a dict
create_contract_payload_dict = create_contract_payload_instance.to_dict()
# create an instance of CreateContractPayload from a dict
create_contract_payload_form_dict = create_contract_payload.from_dict(create_contract_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


