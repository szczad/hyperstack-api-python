# Templates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**templates** | [**List[TemplateFields]**](TemplateFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.templates import Templates

# TODO update the JSON string below
json = "{}"
# create an instance of Templates from a JSON string
templates_instance = Templates.from_json(json)
# print the JSON string representation of the object
print(Templates.to_json())

# convert the object into a dict
templates_dict = templates_instance.to_dict()
# create an instance of Templates from a dict
templates_form_dict = templates.from_dict(templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


