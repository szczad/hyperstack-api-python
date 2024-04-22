# InstanceEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instance_events** | [**List[InstanceEventsFields]**](InstanceEventsFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instance_events import InstanceEvents

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceEvents from a JSON string
instance_events_instance = InstanceEvents.from_json(json)
# print the JSON string representation of the object
print(InstanceEvents.to_json())

# convert the object into a dict
instance_events_dict = instance_events_instance.to_dict()
# create an instance of InstanceEvents from a dict
instance_events_form_dict = instance_events.from_dict(instance_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


