# InviteFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.invite_fields import InviteFields

# TODO update the JSON string below
json = "{}"
# create an instance of InviteFields from a JSON string
invite_fields_instance = InviteFields.from_json(json)
# print the JSON string representation of the object
print(InviteFields.to_json())

# convert the object into a dict
invite_fields_dict = invite_fields_instance.to_dict()
# create an instance of InviteFields from a dict
invite_fields_form_dict = invite_fields.from_dict(invite_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


