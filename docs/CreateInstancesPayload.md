# CreateInstancesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**environment_name** | **str** |  | 
**image_name** | **str** |  | [optional] 
**volume_name** | **str** |  | [optional] 
**create_bootable_volume** | **bool** |  | [optional] 
**flavor_name** | **str** |  | [optional] 
**flavor** | [**FlavorObjectFields**](FlavorObjectFields.md) |  | [optional] 
**key_name** | **str** |  | 
**user_data** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**assign_floating_ip** | **bool** |  | [optional] 
**profile** | [**ProfileObjectFields**](ProfileObjectFields.md) |  | [optional] 
**count** | **int** |  | 

## Example

```python
from hyperstack.models.create_instances_payload import CreateInstancesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstancesPayload from a JSON string
create_instances_payload_instance = CreateInstancesPayload.from_json(json)
# print the JSON string representation of the object
print CreateInstancesPayload.to_json()

# convert the object into a dict
create_instances_payload_dict = create_instances_payload_instance.to_dict()
# create an instance of CreateInstancesPayload from a dict
create_instances_payload_form_dict = create_instances_payload.from_dict(create_instances_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


