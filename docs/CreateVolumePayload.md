# CreateVolumePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 
**callback_url** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.create_volume_payload import CreateVolumePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVolumePayload from a JSON string
create_volume_payload_instance = CreateVolumePayload.from_json(json)
# print the JSON string representation of the object
print CreateVolumePayload.to_json()

# convert the object into a dict
create_volume_payload_dict = create_volume_payload_instance.to_dict()
# create an instance of CreateVolumePayload from a dict
create_volume_payload_form_dict = create_volume_payload.from_dict(create_volume_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


