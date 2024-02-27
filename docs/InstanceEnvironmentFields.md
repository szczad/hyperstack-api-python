# InstanceEnvironmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.instance_environment_fields import InstanceEnvironmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceEnvironmentFields from a JSON string
instance_environment_fields_instance = InstanceEnvironmentFields.from_json(json)
# print the JSON string representation of the object
print InstanceEnvironmentFields.to_json()

# convert the object into a dict
instance_environment_fields_dict = instance_environment_fields_instance.to_dict()
# create an instance of InstanceEnvironmentFields from a dict
instance_environment_fields_form_dict = instance_environment_fields.from_dict(instance_environment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


