# InstanceEventsFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.instance_events_fields import InstanceEventsFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceEventsFields from a JSON string
instance_events_fields_instance = InstanceEventsFields.from_json(json)
# print the JSON string representation of the object
print(InstanceEventsFields.to_json())

# convert the object into a dict
instance_events_fields_dict = instance_events_fields_instance.to_dict()
# create an instance of InstanceEventsFields from a dict
instance_events_fields_form_dict = instance_events_fields.from_dict(instance_events_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


