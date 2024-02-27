# APIKeyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.api_key_fields import APIKeyFields

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyFields from a JSON string
api_key_fields_instance = APIKeyFields.from_json(json)
# print the JSON string representation of the object
print APIKeyFields.to_json()

# convert the object into a dict
api_key_fields_dict = api_key_fields_instance.to_dict()
# create an instance of APIKeyFields from a dict
api_key_fields_form_dict = api_key_fields.from_dict(api_key_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


