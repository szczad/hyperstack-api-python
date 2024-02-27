# Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instance** | [**InstanceAdminFields**](InstanceAdminFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print Instance.to_json()

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_form_dict = instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


