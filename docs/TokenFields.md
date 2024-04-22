# TokenFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**id_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.token_fields import TokenFields

# TODO update the JSON string below
json = "{}"
# create an instance of TokenFields from a JSON string
token_fields_instance = TokenFields.from_json(json)
# print the JSON string representation of the object
print(TokenFields.to_json())

# convert the object into a dict
token_fields_dict = token_fields_instance.to_dict()
# create an instance of TokenFields from a dict
token_fields_form_dict = token_fields.from_dict(token_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


