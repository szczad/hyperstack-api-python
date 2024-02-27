# Instances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instances** | [**List[InstanceAdminFields]**](InstanceAdminFields.md) |  | [optional] 
**instance_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.instances import Instances

# TODO update the JSON string below
json = "{}"
# create an instance of Instances from a JSON string
instances_instance = Instances.from_json(json)
# print the JSON string representation of the object
print Instances.to_json()

# convert the object into a dict
instances_dict = instances_instance.to_dict()
# create an instance of Instances from a dict
instances_form_dict = instances.from_dict(instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


