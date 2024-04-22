# UpdateContractPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**discount_resources** | [**List[ResourcePayload]**](ResourcePayload.md) |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | 

## Example

```python
from hyperstack.models.update_contract_payload import UpdateContractPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContractPayload from a JSON string
update_contract_payload_instance = UpdateContractPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateContractPayload.to_json())

# convert the object into a dict
update_contract_payload_dict = update_contract_payload_instance.to_dict()
# create an instance of UpdateContractPayload from a dict
update_contract_payload_form_dict = update_contract_payload.from_dict(update_contract_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


