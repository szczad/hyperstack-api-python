# InternalInstanceImageFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.internal_instance_image_fields import InternalInstanceImageFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalInstanceImageFields from a JSON string
internal_instance_image_fields_instance = InternalInstanceImageFields.from_json(json)
# print the JSON string representation of the object
print(InternalInstanceImageFields.to_json())

# convert the object into a dict
internal_instance_image_fields_dict = internal_instance_image_fields_instance.to_dict()
# create an instance of InternalInstanceImageFields from a dict
internal_instance_image_fields_form_dict = internal_instance_image_fields.from_dict(internal_instance_image_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


