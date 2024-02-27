# ApiKeyVerifyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_role** | **str** |  | [optional] 
**sub** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.api_key_verify_fields import ApiKeyVerifyFields

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyVerifyFields from a JSON string
api_key_verify_fields_instance = ApiKeyVerifyFields.from_json(json)
# print the JSON string representation of the object
print ApiKeyVerifyFields.to_json()

# convert the object into a dict
api_key_verify_fields_dict = api_key_verify_fields_instance.to_dict()
# create an instance of ApiKeyVerifyFields from a dict
api_key_verify_fields_form_dict = api_key_verify_fields.from_dict(api_key_verify_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


