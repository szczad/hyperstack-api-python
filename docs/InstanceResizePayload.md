# InstanceResizePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavor_name** | **str** |  | [optional] 
**flavor** | [**FlavorObjectFields**](FlavorObjectFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instance_resize_payload import InstanceResizePayload

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceResizePayload from a JSON string
instance_resize_payload_instance = InstanceResizePayload.from_json(json)
# print the JSON string representation of the object
print InstanceResizePayload.to_json()

# convert the object into a dict
instance_resize_payload_dict = instance_resize_payload_instance.to_dict()
# create an instance of InstanceResizePayload from a dict
instance_resize_payload_form_dict = instance_resize_payload.from_dict(instance_resize_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


