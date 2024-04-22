# KeypairFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.keypair_fields import KeypairFields

# TODO update the JSON string below
json = "{}"
# create an instance of KeypairFields from a JSON string
keypair_fields_instance = KeypairFields.from_json(json)
# print the JSON string representation of the object
print(KeypairFields.to_json())

# convert the object into a dict
keypair_fields_dict = keypair_fields_instance.to_dict()
# create an instance of KeypairFields from a dict
keypair_fields_form_dict = keypair_fields.from_dict(keypair_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


