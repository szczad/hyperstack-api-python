# TemplateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.template_fields import TemplateFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFields from a JSON string
template_fields_instance = TemplateFields.from_json(json)
# print the JSON string representation of the object
print TemplateFields.to_json()

# convert the object into a dict
template_fields_dict = template_fields_instance.to_dict()
# create an instance of TemplateFields from a dict
template_fields_form_dict = template_fields.from_dict(template_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


