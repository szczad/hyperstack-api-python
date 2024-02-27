# UpdateTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.update_template import UpdateTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplate from a JSON string
update_template_instance = UpdateTemplate.from_json(json)
# print the JSON string representation of the object
print UpdateTemplate.to_json()

# convert the object into a dict
update_template_dict = update_template_instance.to_dict()
# create an instance of UpdateTemplate from a dict
update_template_form_dict = update_template.from_dict(update_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


